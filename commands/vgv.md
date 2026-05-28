---
name: vgv
description: VGV-Analyse - automatische Vertragsrisiko- und Vergabe-Bewertung fuer Architektur- und Planungsbueros bei oeffentlichen Vergabeverfahren. Liest alle Vergabeunterlagen (Bekanntmachung, Vertragsmuster, Bewerbungsbedingungen, Anlagen), bewertet rollenspezifische Risiken (Honorarklauseln, Haftung, Referenzanforderungen, etc.) und erzeugt eine Standalone-HTML-Analyse mit Risiko-Ampel und Verhandlungs-Empfehlungen.
user-invocable: true
---

# VGV-Analyse Skill

## OUTPUT-KONVENTION (verbindlich)

**EINZIGE REGEL: Du legst NUR Dateien im `Claude/`-Ordner des Projekt-Roots ab. NIRGENDS sonst im Projekt.**

```
<Projekt-Root>/                           <- bleibt unveraendert
└── Claude/                               <- EINZIGER Ordner den wir anlegen
    └── VGV-Analyse/
        ├── VGV_Analyse_2026-05-27.html   <- DEIN OUTPUT
        └── VGV_Analyse_2026-06-15.html   (spaeterer Aufruf = neue Datei)
```

**Dein Output-Pfad:** `<Projekt-Root>/Claude/VGV-Analyse/VGV_Analyse_{YYYY-MM-DD}.html`

**Pflichten:**
1. `<Projekt-Root>/Claude/VGV-Analyse/` anlegen falls nicht vorhanden
2. Aktuelles Datum im Dateinamen (YYYY-MM-DD)
3. Bei jedem Aufruf: NEUE Datei (keine Ueberschreibung)

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

Speichere die Antworten in `<USER-HOME>/.claude/buero.json` (so muss der User es nur EINMAL ausfuellen, fuer alle zukuenftigen VGV-Analysen).

### Schritt 2: Projektordner identifizieren

- Standardmaessig ist das aktuelle Arbeitsverzeichnis (`pwd`) der Projektordner
- Falls Argumente uebergeben wurden (`$ARGUMENTS`), nimm den dort angegebenen Pfad
- Falls keine VGV-Unterlagen (PDFs, Word, Vertragsentwurf, Bekanntmachung) im aktuellen Ordner: frage den Nutzer wo die Unterlagen liegen

### Schritt 3: Analyse durchfuehren

- Fuehre alle Schritte aus `vgv-analyse_tools/ANLEITUNG.md` durch (Schritt 0 bis Schritt 10)
- **Wichtig**: Machbarkeitsstudien VOLLSTAENDIG lesen (Schritt 1b-KRITISCH in der ANLEITUNG)
- Wende rollenspezifische Anweisungen aus dem geladenen Profil an

### Schritt 4: Output erstellen

- Erstelle die HTML-Analyse in `<Projekt-Root>/Claude/VGV-Analyse/VGV_Analyse_{YYYY-MM-DD}.html`
- Standalone HTML mit Branding aus `buero.json`
- PDF-Export-Button und Inline-Bearbeitungsmodus integriert
- Qualitaetsniveau: Big-4-Beratung

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

- Outputs ausserhalb von `<Projekt-Root>/Claude/` schreiben
- Vertragsklauseln oder Honoraransaetze erfinden
- Rechtsberatung erteilen (du bist Tool, nicht Anwalt - immer Hinweis im Bericht)
- Marcels Buero-Daten verwenden falls eine andere buero.json vorhanden ist
