---
name: vgv-praesentation
description: Baut mit der Nutzerin / dem Nutzer zusammen eine GHIW-Präsentation für das Verhandlungsgespräch (VgV Phase 2) – aus Foliendatenbank, Projektbild-Datenbank, Referenzdatenbank und den Unterlagen des Verfahrens, im verbindlichen GHIW-Gestaltungs- und Sprachstandard, als bearbeitbare PowerPoint-Datei. Triggert IMMER bei "VgV-Präsentation", "Präsentation für das Verhandlungsgespräch", "Vortrag Phase 2", "Präsentation für das Verfahren X", "Angebotspräsentation", "wir sind eingeladen, bau die Präsentation", "nutze das GHIW-Board für die Präsentation", "welche alten Folien passen zu …". NICHT für Referenzblätter (Skill referenzblatt), schriftliche Gesamtkonzepte ohne Vortrag und die VgV-Analyse (/vgv).
---

# GHIW-Präsentation für das Verhandlungsgespräch

Ziel ist eine Präsentation, die besser ist als alles, was das Büro bisher gezeigt hat: ruhig, klar, architektonisch –
und inhaltlich so nah am Auftraggeber, dass das Gremium denkt: *„stimmt, das wird passieren – die wissen das“*.
Das Büro stellt sich weiter vor, aber nicht mehr als Hauptsache. Kundennähe entsteht **subtil**: Probleme des
Auftraggebers werden als Befund aus eigener Erfahrung benannt, mit Folge und Maßnahme – nie als Frage, nie anbiedernd.

**Verbindlich, vor allem anderen lesen:**
`N:\13. VGV\1-Vorlagen\02_Vorlagen-Präsentation-Phase2\00-Foliendatenbank\GESTALTUNG_UND_SPRACHE.md`
(Raster, Typografie, Farben, Bild- und Diagrammsprache, Titelregeln, verbotene Wendungen, Dramaturgie der Zusagen 2026).
Gebaut wird nur mit dem Baukasten `agentic-os\folien\baukasten\` (Muster und Datenfelder: `…\00-Foliendatenbank\BAUKASTEN.md`).
Du gestaltest nichts frei: keine eigenen Farben, Formen, Icons, Häkchen, Kennzeichen wie „B1“, keine Folien als HTML.

## Werkzeuge

- **GHIW-Board (MCP):** `folien_ueberblick`, `folien_suche` (Volltext + Filter `muster`, `folientyp`, `bewertung`, `jahr_ab`), `folie` (eine Folie mit allen Vorkommen), `projektbilder_suche` (zeigbare Fotos je Projekt und Motiv); dazu die VgV-Werkzeuge des Boards (`vgv_dashboard`, `ausschreibungen_suche`) für die Radar-Karte des Verfahrens.
- **Ohne Board-Verbindung (Claude Code im Büro):** dieselben Tabellen über `node db/frag.mjs "<sql>"` im Ordner `agentic-os` (Tabellen `folien`, `praesentationen`, `projektbilder`).
- **Folienbilder** liegen unter `N:\13. VGV\1-Vorlagen\02_Vorlagen-Präsentation-Phase2\00-Foliendatenbank\folien\<schluessel>\sNNN.jpg`; die Galerie dort (`index.html`) zeigt alles mit Filtern.
- **Referenzdatenbank:** `N:\13. VGV\7-Referenzdatenbank\projekte\<id>.md` (Fakten mit Quelle).

## Schritt 1 – Rückfragen (immer zuerst, eine Abfrage)

Mit **einer** AskUserQuestion-Abfrage (sonst eine kurze nummerierte Frage), nur was noch nicht gesagt ist:
1. **Welches Verfahren?** Ordner unter `N:\13. VGV\2-Laufende VgV\` oder Radar-Karte.
2. **Termin, Redezeit, Folienzahl?** (Richtwert der Zusagen 2026: 20–35 Folien für 30 Minuten.)
3. **Wer präsentiert, wer ist Projektleitung/Stellvertretung, Konstellation (GHIW allein / ARGE mit …)?**
4. **Wie viel Büro, wie viel Projekt?** – wie bisher · Büro knapp, Schwerpunkt Projekt (empfohlen) · nur Projekt.

## Schritt 2 – Lage des Verfahrens erfassen (nichts erfinden)

Aus dem Verfahrensordner: Aufforderung zum Verhandlungsgespräch / Angebotsaufforderung, **Zuschlagskriterien mit Gewichtung** (Wertungsmatrix), Aufgabenbeschreibung, Vertragsentwurf, Bieterantworten, `5-Analyse\*` (VGV-Analyse, Referenz-Analyse). Dazu Radar-Karte im Board und Ortskenntnis (Luftbild, Lageplan aus den Unterlagen).

Lege intern (nicht als Folie) fest:
- **Die 4–6 Anliegen des Auftraggebers**, jeweils mit Quelle (Seite).
- **Die Probleme, auf die er stoßen wird**, jeweils als Befund → Folge → Maßnahme, belegt mit einem eigenen Projekt und einer Zahl (Foliendatenbank `folien_suche` mit `folientyp: qualitaet` / Muster `matrix_tabelle`; Referenzdatenbank; frühere Konzepte im Archiv).

## Schritt 3 – Struktur vorschlagen und abstimmen

Gliederung = Zuschlagskriterien in ihrer Reihenfolge. Projektbezug spätestens auf Folie 3–5. Am Ende jedes Kriteriums ein Kernbotschaft-Band. Schluss nach GHIW-Standard.

Zeige die Struktur als Tabelle: **Nr. · Kapitel · Folientitel (GHIW-Ton) · Muster · Inhalt in einem Satz · Quelle** – Quelle ist entweder eine Folie der Datenbank (`folie`-ID, Verfahren, Jahr, Seite; Bewertung) oder „neu“.
Für jede Zeile vorher `folien_suche` nutzen: bevorzugt Folien mit Bewertung *wiederverwenden*/*anpassen* und hoher `gestaltung_note`; ihr Muster übernehmen, Inhalt auf das Verfahren übertragen (Feld `uebertragung`).
Dann fragen: passt die Struktur – oder was ändern? Erst nach Zustimmung weiter.

## Schritt 4 – Referenzen und Fotos abstimmen

- Referenzen **je Anliegen** wählen (nicht nach Größe): Fakten aus der Referenzdatenbank, je Referenz der Satz „was das für dieses Projekt heißt“.
- Fotos mit `projektbilder_suche` (nur zeigbar, beste Fassung). Claude trifft hier erfahrungsgemäß etwa 80 %, der Rest passt nicht – **deshalb immer** einen Kontaktbogen der vorgeschlagenen Fotos und der wiederverwendeten Altfolien bauen (PIL, 3×3, mit Nummer) und mit `SendUserFile` zeigen. Fragen: welche ersetzen, welche anders darstellen? Ersatz aus derselben Suche oder vom Nutzer genannt.
- Luftbilder, Lagepläne, Pläne des Auftraggebers: nur aus den Vergabeunterlagen, Quelle in der Bildunterschrift.

## Schritt 5 – Bauen

1. `plan.json` nach `BAUKASTEN.md` schreiben: je Folie Muster, Kapitel, Titel, Inhalt, Bilder, **Sprechertext** (`notiz`).
2. `python -I -X utf8 agentic-os\folien\baukasten\bauen.py plan.json <Verfahren>\3-Phase_2\2-Indesign_Präsentation\Präsentation_<Kurzname>_ENTWURF.pptx --png <ordner>` – der Prüfbericht muss ohne Fehler sein (kein Textüberlauf, nichts außerhalb der Folie, alle Bilder da).
3. **Sprachprüfung** gegen die Liste verbotener Wendungen im Leitfaden: keine Anrede („Sie“, „Ihr“) in Titeln, keine Fragen als Titel, keine Formeln „X statt Y“ / „X – deshalb Y“, keine Superlative ohne Beleg.
4. Die PNGs selbst ansehen (Kontaktbogen) – sieht es aus wie die Vorbilder im Leitfaden? Sonst nachbessern.
5. PPTX und Kontaktbogen mit `SendUserFile` zeigen; Änderungswünsche einarbeiten, bis freigegeben. Alles bleibt in PowerPoint bearbeitbar; übernommene Altfolien ohne Vorlage im Baukasten kommen als Bild (Muster `archiv`) und sind entsprechend markiert.

## Was nie passiert

- Titel wie „Wo können wir Ihnen helfen?“, „Was Sie von uns erwarten können“, „Ihr Bedarf – unsere Zusage“.
- Selbstlob ohne Beleg („langjährige Erfahrung“, „höchste Qualität“) – stattdessen Projekt + Zahl.
- Unlesbare Screenshots (Excel, Terminpläne in Kleinstschrift) – stattdessen Baukasten-Muster mit den Kernzahlen.
- Fotos, die nicht als zeigbar markiert sind, ohne ausdrückliche Freigabe.
