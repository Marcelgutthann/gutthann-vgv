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

Und erzeugt eine **Standalone-HTML-Analyse** mit:
- Vertragsklauseln-Bewertung (Risiko-Ampel)
- Honorar-Plausibilitaet
- Referenz-Eignung (kannst du die Referenz erfuellen?)
- Risiken pro Rolle (rollenspezifisch)
- Verhandlungs-Empfehlungen
- Empfehlung: Teilnahme ja/nein

Output: `<Projekt-Root>/Claude/VGV-Analyse/VGV_Analyse_YYYY-MM-DD.html`

## Universell fuer jedes Architekturbuero

Beim ersten Aufruf fragt der Skill nach deinen Buero-Daten:
- Bueroname
- Leistungsbild (Architektur / Generalplaner / Bauingenieur / Innenarchitektur / Landschaft / ...)
- Buerogroesse
- Adresse, Kontakt
- CAD-System
- Logo + Branding-Farben

Diese werden in `~/.claude/buero.json` gespeichert - musst du nur **einmalig** ausfuellen, fuer alle zukuenftigen VGV-Analysen.

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

Dann startet die Analyse automatisch. Output erscheint in `Claude/VGV-Analyse/`.

## Output-Konvention

Alle Outputs landen in `<Projekt-Root>/Claude/VGV-Analyse/`. Die bestehende Projekt-Struktur wird **nicht angefasst**.
