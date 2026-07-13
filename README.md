# VGV - Vergabe-Verfahrens-Analyse fuer Architekten

> Plugin fuer Claude Code. Automatische Vertragsrisiko- und VGV-Bewertung fuer Architektur- und Planungsbueros bei oeffentlichen Vergabeverfahren.

## Was es macht

Wenn du in einem Projektordner mit VGV-Unterlagen `/vgv` eintippst, durchsucht Claude:
- Bekanntmachung (EU-Auftragsbekanntmachung)
- Vertragsmuster (HAV-KOM, RBBau, individuelle Vertraege)
- Bewerbungsbedingungen
- Eignungskriterien / Referenzanforderungen
- Honorartafeln / Preisangaben
- Bauherrnbeschreibung
- Machbarkeitsstudien (komplett, auch grosse PDFs)
- Anlagen (Plaene, Lageplaene, B-Plan)

Und erzeugt **Standalone-HTML-Dateien** im Ordner `5 Analyse/`:

1. **`VGV_Analyse_YYYY-MM-DD.html`** - die Hauptanalyse:
   - Vertragsklauseln-Bewertung (Risiko-Ampel)
   - Honorar-Plausibilitaet
   - Referenz-Eignung (kannst du die Referenz erfuellen?)
   - Risiken pro Rolle (rollenspezifisch)
   - Verhandlungs-Empfehlungen
   - Empfehlung: Teilnahme ja/nein
2. **`Referenz_Analyse_YYYY-MM-DD.html`** - Referenz-Empfehlungen aus der Buero-Referenzdatenbank (optional, ab v1.1)
3. **`TERMINE.html`** - alle Termine und Fristen aufbereitet, mit Live-Countdown; fester Dateiname, damit sie immer am selben Ort zu finden ist (ab v1.1)

## Referenz-Matching (ab v1.1, optional)

Wenn in der `buero.json` ein Pfad zu einer buero-weiten Referenzdatenbank hinterlegt ist (`"referenzdatenbank": "N:\\...\\Referenzdatenbank"`), schlaegt der Skill nach der Analyse der Referenzanforderungen automatisch die passendsten eigenen Projekte als Referenzen vor - inklusive empfohlenem Zuschnitt (welche Leistungsphasen darstellen, welche Kostenbasis, welches Narrativ), wie es Projektleiter beim "Zurechtlegen" von Referenzen auch tun.

Dabei gelten harte Regeln: Auswahl und Betonung real erbrachter Leistungen ist erlaubt, Faktenaenderung (Kosten, Flaechen, LPH, Termine) ist verboten, Grenzfaelle werden zur Ruecksprache markiert. Die Datenbank wird nur gelesen, nie beschrieben.

Erwartete Datenbank-Struktur: ein Ordner mit `SCHEMA.md`, `INDEX.md`, `projekte\*.md` (YAML-Frontmatter + Prosa), optional `referenz-instanzen\` und `verfahren\` (Anpassungshistorie frueherer Bewerbungen). Ohne konfigurierte Datenbank wird der Schritt einfach uebersprungen.

**GHIW-intern:** Die Buero-Referenzdatenbank liegt unter `N:\13. VGV\7-Referenzdatenbank` (176 Projekte, 226 Verfahren, Referenz-Instanzen). Der Skill erkennt diesen Pfad automatisch, wenn das N:-Laufwerk verbunden ist - es ist KEINE Konfiguration noetig. Wer den Pfad manuell setzen will: `"referenzdatenbank": "N:\\13. VGV\\7-Referenzdatenbank"` in der `buero.json`.

## Universell fuer jedes Architekturbuero

Beim ersten Aufruf fragt der Skill nach deinen Buero-Daten:
- Bueroname
- Leistungsbild (Architektur / Generalplaner / Bauingenieur / Innenarchitektur / Landschaft / ...)
- Buerogroesse
- Adresse, Kontakt
- CAD-System
- Logo + Branding-Farben

Diese werden in `~/.claude/buero.json` gespeichert - musst du nur **einmalig** ausfuellen, fuer alle zukuenftigen VGV-Analysen.

## Bewerber-Konstellation (Suchprofile, ab v1.2)

Beim Start jeder Analyse fragt der Skill, WER sich bewirbt:

1. **GHIW / Einzelbewerbung** - das eigene Buero allein
2. **AIP Generalplanergesellschaft** - Bewerbung ueber die GP-Gesellschaft
3. **ARGE / Bewerbergemeinschaft** - gemeinsam mit einem Partner

Bei AIP und ARGE folgt eine zweite Frage nach dem Namen der anderen Gesellschaft, danach immer die Frage, ob es relevante und zu beachtende Referenzen oder Informationen gibt. Die Antworten werden pro Projekt in `Claude/bewerbung.json` gespeichert (Re-Runs fragen nicht erneut) und steuern ein konstellationsspezifisches Suchprofil aus `vgv-analyse_tools/bewerberprofile/`: Zulassung der Konstellation, Bewerbergemeinschaftserklaerung, gesamtschuldnerische Haftung, Eignungsleihe, wessen Referenzen zaehlen, Nachweise je Mitglied usw.

## Verfuegbare Rollen-Profile

In `vgv-analyse_tools/profiles/`:

| Profil | Status |
|---|---|
| `architekt.md` (Objektplanung Gebaeude/Innenraeume) | v1.0 verfuegbar |
| `generalplaner.md` | folgt in v2.0 |
| `bauingenieur.md` (mit Sub-Disziplinen: Tragwerk, TGA, Bauphysik, Brandschutz, Tiefbau, Geotechnik) | folgt in v2.0 |
| `innenarchitekt.md` | folgt |
| `landschaftsarchitekt.md` | folgt |

Falls dein Leistungsbild noch nicht abgedeckt ist, wirst du gefragt ob die Analyse generisch durchgefuehrt werden soll.

## Installation

```
/plugin marketplace add github:Marcelgutthann/gutthann-claude-marketplace
/plugin install vgv
```

Nach der Installation: Claude Code einmal neu starten.

## Erstmaliger Aufruf

```
/vgv
```

Claude fragt dich:
1. **Wo liegen die VGV-Unterlagen?** (Standardmaessig aktueller Ordner)
2. **Buero-Daten** (falls noch keine `buero.json`) - nur einmal!
3. **Bewerber-Konstellation** (GHIW / AIP / ARGE, siehe oben) - einmal pro Projekt, gespeichert in `Claude/bewerbung.json`

Dann startet die Analyse automatisch. Output erscheint in `5 Analyse/`.

## Output-Konvention

Alle Outputs landen in `<Projekt-Root>/5 Analyse/` (wird bei Arbeitsbeginn angelegt). Ansonsten wird die bestehende Projekt-Struktur **nicht angefasst**. Analyse-Dateien werden nie ueberschrieben (neues Datum = neue Datei); einzige Ausnahme ist `TERMINE.html`, die bei jedem Lauf aktualisiert wird.
