"""GHIW-Referenzblatt bauen: Logo + Bilder einsetzen, PDF drucken, prüfen.

Aufruf:  python bauen.py <entwurf.html> [--ziel <ordner>]
Ergebnis: <name>.html (bearbeitbar, Bilder eingebettet) + <name>.pdf im Zielordner
          (Standard: Ordner des Entwurfs). Exit-Code 1, wenn eine Prüfung scheitert.

Prüfungen (alle müssen grün sein, sonst ist das Blatt nicht fertig):
  1. keine {{Platzhalter}} mehr übrig
  2. jedes Bild aus data-src gefunden und eingebettet
  3. kein Textfeld läuft über (Editor-Prüfung im Browser, wie beim Drucken)
  4. PDF hat genau so viele Seiten wie <section class="page">
Offene Werte ([zu ergänzen …]) sind erlaubt, werden aber gezählt und gemeldet.
"""
import base64, io, json, os, re, subprocess, sys, tempfile

HIER = os.path.dirname(os.path.abspath(__file__))
EDGE = [r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe"]
MAX_PX = 2400   # längste Bildkante; reicht für A4-Druck, hält die Datei unter ~5 MB


def bild_data_uri(pfad):
    seite = 1
    m = re.match(r"(.*\.pdf)#(\d+)$", pfad, re.I)
    if m:
        pfad, seite = m.group(1), int(m.group(2))
    if not os.path.exists(pfad):
        return None
    from PIL import Image
    if pfad.lower().endswith(".pdf"):
        import fitz
        doc = fitz.open(pfad)
        p = doc[seite - 1]
        zoom = min(4.0, MAX_PX / max(p.rect.width, p.rect.height))
        img = Image.open(io.BytesIO(p.get_pixmap(matrix=fitz.Matrix(zoom, zoom)).tobytes("png")))
    else:
        img = Image.open(pfad)
    img = img.convert("RGB")
    img.thumbnail((MAX_PX, MAX_PX))
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=82, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def browser():
    for p in EDGE:
        if os.path.exists(p):
            return p
    sys.exit("Kein Edge/Chrome gefunden – PDF kann nicht gedruckt werden.")


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    quelle = os.path.abspath(args[0])
    ziel = os.path.abspath(args[args.index("--ziel") + 1]) if "--ziel" in args else os.path.dirname(quelle)
    name = os.path.splitext(os.path.basename(quelle))[0].removesuffix("_entwurf")
    html = open(quelle, encoding="utf-8").read()
    fehler = []

    # Seitentitel und Dateiname setzt das Skript selbst
    h1 = re.search(r'<h1 class="title"[^>]*>(.*?)(<small|</h1>)', html, re.S)
    titel = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else name
    html = html.replace("{{TITEL_KURZ}}", titel).replace("{{DATEINAME}}", name + ".html")

    # Anleitungskommentare der Vorlage zählen nicht als Inhalt
    inhalt = re.sub(r"<!--.*?-->", "", html, flags=re.S)

    # 1. Platzhalter
    rest = sorted(set(re.findall(r"\{\{[^}]*\}\}", inhalt)))
    if rest:
        fehler.append(f"{len(rest)} Platzhalter offen: " + ", ".join(rest[:8]))

    # Logo
    logo = open(os.path.join(HIER, "logo.svg"), encoding="utf-8").read().strip()
    html = html.replace('<div class="logo"></div>', f'<div class="logo">{logo}</div>')

    # 2. Bilder
    bilder = {}
    for key, src in re.findall(r'data-img="([^"]+)"\s+data-src="([^"]+)"', html):
        uri = bild_data_uri(src)
        if uri:
            bilder[key] = uri
        else:
            fehler.append(f"Bild fehlt: {key} → {src}")
    html = re.sub(r'<script id="imgdata" type="application/json">.*?</script>',
                  lambda _: '<script id="imgdata" type="application/json">' + json.dumps(bilder) + "</script>",
                  html, flags=re.S)
    html = re.sub(r'var FILENAME=".*?";', f'var FILENAME="{name}.html";', html)

    os.makedirs(ziel, exist_ok=True)
    out_html = os.path.join(ziel, name + ".html")
    out_pdf = os.path.join(ziel, name + ".pdf")
    open(out_html, "w", encoding="utf-8").write(html)

    # 3. Überlauf: DOM nach dem Laden (checkPages markiert .overflow)
    exe = browser()
    with tempfile.TemporaryDirectory() as prof:
        base = [exe, "--headless=new", "--disable-gpu", "--no-first-run", f"--user-data-dir={prof}",
                "--virtual-time-budget=8000"]
        dom = subprocess.run(base + ["--dump-dom", out_html], capture_output=True, text=True,
                             encoding="utf-8", errors="replace", timeout=120).stdout
        n_over = len(re.findall(r'class="[^"]*\boverflow\b', dom.split('<div id="doc">', 1)[-1]))
        if n_over:
            fehler.append(f"{n_over} Textfeld(er) laufen über – Text kürzen")
        # 4. PDF
        subprocess.run(base + ["--no-pdf-header-footer", f"--print-to-pdf={out_pdf}", out_html],
                       capture_output=True, timeout=180)

    n_sec = html.count('<section class="page"')
    if not os.path.exists(out_pdf):
        fehler.append("PDF wurde nicht erzeugt")
    else:
        import fitz
        n_pdf = fitz.open(out_pdf).page_count
        if n_pdf != n_sec:
            fehler.append(f"PDF hat {n_pdf} Seiten, Blatt hat {n_sec} – etwas sprengt das A4-Raster")

    offen = len(re.findall(r"\[zu ergänzen", inhalt))
    print(f"HTML: {out_html}\nPDF:  {out_pdf}")
    print(f"Seiten: {n_sec} · Bilder eingebettet: {len(bilder)} · offene Werte [zu ergänzen]: {offen}")
    if fehler:
        print("NICHT FERTIG:\n  - " + "\n  - ".join(fehler))
        sys.exit(1)
    print("Alle Prüfungen grün.")


if __name__ == "__main__":
    main()
