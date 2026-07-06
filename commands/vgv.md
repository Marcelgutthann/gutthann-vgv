---
name: vgv
description: VGV-Analyse - automatische Vertragsrisiko- und Vergabe-Bewertung fuer Architektur- und Planungsbueros bei oeffentlichen Vergabeverfahren. Liest alle Vergabeunterlagen (Bekanntmachung, Vertragsmuster, Bewerbungsbedingungen, Anlagen), bewertet rollenspezifische Risiken (Honorarklauseln, Haftung, Referenzanforderungen, etc.) und erzeugt Standalone-HTML-Dateien im Ordner "5 Analyse" - Hauptanalyse mit Risiko-Ampel und Verhandlungs-Empfehlungen, optional Referenz-Empfehlungen aus der Buero-Referenzdatenbank, und eine Terminuebersicht (TERMINE.html).
user-invocable: true
---

# VGV-Analyse Skill

## OUTPUT-KONVENTION (verbindlich)

**EINZIGE REGEL: Du legst NUR Dateien im Ordner `5 Analyse` des Projekt-Roots ab. NIRGENDS sonst im Projekt.**

```
<Projekt-Root>/                                <- bleibt unveraendert
└── 5 Analyse/                                 <- EINZIGER Ordner den wir anlegen
    ├── VGV_Analyse_2026-05-27.html            <- Hauptanalyse (wie gehabt)
    ├── Referenz_Analyse_2026-05-27.html       <- Referenz-Empfehlungen (nur falls Referenzdatenbank konfiguriert)
    └── TERMINE.html                           <- alle Termine/Fristen (fester Name, wird aktualisiert)
```

**Pflichten:**
1. `<Projekt-Root>/5 Analyse/` SOFORT bei Arbeitsbeginn anlegen (falls nicht vorhanden)
2. Aktuelles Datum im Dateinamen der Analyse-Dateien (YYYY-MM-DD)
3. Bei jedem Aufruf: NEUE Analyse-Dateien (keine Ueberschreibung). Einzige Ausnahme: `TERMINE.html` hat bewusst einen FESTEN Dateinamen und wird bei jedem Lauf komplett neu geschrieben, damit das Team sie immer am selben Ort findet.

**NIE:** in andere Projekt-Ordner, in `~/.claude/plugins/`, in versteckte Ordner.

---

## Was zu tun ist

### Schritt 1: Konfiguration laden

Lies aus dem Plugin-Ordner:
- `vgv-analyse_tools/ANLEITUNG.md` (komplette Analyse-Anleitung mit 10 Schritten)
- `vgv-analyse_tools/profiles/{leistungsbild}.md` (Rollen-Profil je nach Buerotyp)

Lies die Buero-Konfiguration (eine der folgenden):
- `<Projekt-Root>/Claude/buero.json` (projekt-spezifisch, falls vorhanden - hat Vorrang)
- `<USER-HOME>/.claude/buero.json` (user-globale Konfig, falls vorhanden - Fallback)
- `vgv-analyse_tools/buero.example.json` (Template - wird benutzt zum Anlegen falls noch nichts da)

**Falls keine buero.json existiert:**
Frage den Nutzer interaktiv ab:
- Bueroname
- Leistungsbild (Architekturbuero / Bauingenieurbuero / Generalplaner / Andere)
- Buerogroesse (Solo / 2-5 / 6-20 / >20 Personen)
- Adresse, Telefon, E-Mail
- CAD-System
- Angebotene Leistungsphasen
- Logo-Pfad
- Branding-Farben
- Pfad zur buero-weiten Referenzdatenbank (optional, falls vorhanden - sonst leer lassen)

Speichere die Antworten in `<USER-HOME>/.claude/buero.json` (so muss der User es nur EINMAL ausfuellen, fuer alle zukuenftigen VGV-Analysen).

### Schritt 2: Projektordner identifizieren

- Standardmaessig ist das aktuelle Arbeitsverzeichnis (`pwd`) der Projektordner
- Falls Argumente uebergeben wurden (`$ARGUMENTS`), nimm den dort angegebenen Pfad
- Falls keine VGV-Unterlagen (PDFs, Word, Vertragsentwurf, Bekanntmachung) im aktuellen Ordner: frage den Nutzer wo die Unterlagen liegen

### Schritt 3: Analyse durchfuehren

- Fuehre alle Schritte aus `vgv-analyse_tools/ANLEITUNG.md` durch (Schritt 0 bis Schritt 10)
- **Wichtig**: Machbarkeitsstudien VOLLSTAENDIG lesen (Schritt 1b-KRITISCH in der ANLEITUNG)
- Wende rollenspezifische Anweisungen aus dem geladenen Profil an

### Schritt 4: Referenz-Matching (falls Referenzdatenbank konfiguriert)

Falls in `buero.json` das Feld `buero.referenzdatenbank` gesetzt und der Pfad erreichbar ist:

- Fuehre nach der Referenzanalyse das Referenz-Matching gemaess `vgv-analyse_tools/ANLEITUNG.md` Schritt 4e durch
- Ein Matching-Agent schlaegt pro geforderter Referenz die besten Kandidaten aus der Datenbank vor, inkl. empfohlenem Zuschnitt (welche LPH darstellen, welche Kostenbasis, welches Narrativ)
- **Verhaltensregel:** Zuschnitt innerhalb der Fakten ist erlaubt (Auswahl/Betonung real erbrachter Leistungen), Faktenaenderung ist verboten. Grenzfaelle werden markiert, nicht entschieden. Details in ANLEITUNG.md Schritt 4e.
- Ergebnis wird als EIGENE Datei `5 Analyse/Referenz_Analyse_{YYYY-MM-DD}.html` abgelegt (Details in ANLEITUNG.md Schritt 10b) - NICHT in die Hauptanalyse integriert, damit diese schlank bleibt. Die Hauptanalyse verlinkt darauf.

Falls das Feld fehlt, `null` ist oder der Pfad nicht erreichbar (z.B. Netzlaufwerk nicht verbunden): Schritt ueberspringen und im Bericht kurz vermerken.

### Schritt 5: Output erstellen

Alle Outputs nach `<Projekt-Root>/5 Analyse/`:

1. **`VGV_Analyse_{YYYY-MM-DD}.html`** - die Hauptanalyse, inhaltlich wie gehabt (Struktur siehe ANLEITUNG.md Schritt 10a), mit Verweis-Links auf die beiden anderen Dateien
2. **`Referenz_Analyse_{YYYY-MM-DD}.html`** - nur falls Referenz-Matching gelaufen ist (ANLEITUNG.md Schritt 10b)
3. **`TERMINE.html`** - immer; alle Termine und Fristen aufbereitet, fester Dateiname (ANLEITUNG.md Schritt 10c)

Alle Dateien: Standalone HTML mit Branding aus `buero.json`, PDF-Export-Button und Inline-Bearbeitungsmodus, Qualitaetsniveau Big-4-Beratung.

---

## Profile (Rollen-spezifisch)

Im Plugin enthalten in `vgv-analyse_tools/profiles/`:

| Leistungsbild | Profil-Datei | Status |
|---|---|---|
| Architekturbuero | `profiles/architekt.md` | v1 verfuegbar |
| Generalplaner | `profiles/generalplaner.md` | folgt (V2) |
| Bauingenieurbuero | `profiles/bauingenieur.md` | folgt (V2) |
| Innenarchitektur | `profiles/innenarchitekt.md` | folgt |
| Landschaftsarchitektur | `profiles/landschaftsarchitekt.md` | folgt |

Falls in `buero.json` ein noch nicht abgedecktes Leistungsbild steht:
- Frage den Nutzer ob er die Analyse generisch (ohne Rollenprofil) durchfuehren will
- Bei `ja`: ohne Profil, im Bericht entsprechend ausweisen
- Bei `nein`: Abbruch

---

## Anti-Halluzinations-Regeln

- **Keine Erfindung von Vertragsklauseln.** Nur was in den gelesenen Vergabeunterlagen wirklich steht.
- **Keine Erfindung von Bewertungen.** Bewertung basiert auf HOAI, VgV, VOB, BGB - nicht auf Vermutungen.
- **Bei Unklarheit:** `(Verifikation noetig)` markieren, nicht raten.
- **Quellen-Treue:** jede Aussage mit Quell-Dokument + Seitenzahl belegen.

---

## Was du nie tust

- Outputs ausserhalb von `<Projekt-Root>/5 Analyse/` schreiben
- Vertragsklauseln oder Honoraransaetze erfinden
- Referenz-Fakten veraendern oder erfinden (Kosten, Flaechen, LPH, Termine, Bauherr) - Zuschnitt ja, Faktenaenderung nie
- In die Referenzdatenbank schreiben (sie ist fuer diesen Skill strikt read-only)
- Rechtsberatung erteilen (du bist Tool, nicht Anwalt - immer Hinweis im Bericht)
- Marcels Buero-Daten verwenden falls eine andere buero.json vorhanden ist
