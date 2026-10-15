---
name: referenzblatt
description: Erstellt oder baut ein GHIW-Referenzblatt (Objektdatenblatt/Projektdoku für VgV-Bewerbungen) im festen Hausstil der InDesign-Objektdatenblätter – Logo, Fotos, Pläne, Projektdaten, Kurzbeschreibung, Kriterienmatrix – als bearbeitbares HTML plus PDF. Triggert IMMER bei "Referenzblatt", "Referenz erstellen", "Projektreferenz", "Objektdatenblatt", "Projektdoku für die Bewerbung", "mach mir im Projekt X eine Referenz", "Referenz für das Verfahren Y", und beim Umbauen bestehender Blätter: "bau die Referenz um für Holzbau", "Referenz auf Sanierung zuschneiden", "Referenz kürzen auf eine Seite". NICHT für reine Datenbankpflege der Referenzdatenbank und nicht für die VgV-Gesamtanalyse (/vgv).
---

# GHIW-Referenzblatt

Das Layout ist **fest**. Es kommt aus `vorlage.html` in diesem Skill-Ordner (abgeleitet aus den
Bernhardswald-Blättern vom 14.10.2026, die den InDesign-Objektdatenblättern 1:1 folgen).
Du gestaltest **nichts** neu: keine eigenen Farben, Schriften, Raster, Tabellen- oder Kartenstile,
keine Excel/JSON/Markdown-Ausgabe statt des Blatts. Deine Arbeit ist Inhalt: Fakten finden,
auswählen, auf den Fokus zuschneiden, Bilder wählen.

Muster, wie ein fertiges Blatt aussieht (GHIW-intern, nur lesen):
`N:\13. VGV\2-Laufende VgV\2026_10_21_Grundschule_Bernhardswald\2-Phase_1\2-Teilnahmeunterlagen_Anlagen\2026-10-14_Projektdoku_GS-Bernhardswald_Ref1_MS-BadAbbach-BA2.html` (und `…Ref2_GS-Hagelstadt.html`).
Bei Unsicherheit über Ton, Dichte oder Bildwahl: dort nachsehen.

## Schritt 1 – Rückfragen (immer, vor jeder Suche)

Stelle mit **einer** AskUserQuestion-Abfrage (gibt es das Werkzeug nicht: als eine kurze nummerierte Frage im Chat) diese Fragen (was die Nutzerin schon gesagt hat, nicht erneut fragen):

1. **Wie viele Seiten?** – 1 Seite (nur Seite 1) · 2 Seiten (+ Kriterienmatrix mit großem Plan/Bild) · 3 Seiten (+ Aufgabe und Umsetzung)
2. **Gibt es einen Fokus?** – kein Fokus · Holzbau/Holzhybrid · Sanierung/Bauen im Bestand bei laufendem Betrieb · Schule/Ganztag · (Freitext über „Other“: z. B. Nachhaltigkeit, Barrierefreiheit, Kosten-/Termintreue, Förderung)
3. **Für welches Verfahren?** – für ein laufendes VgV-Verfahren (dann Ordner nennen) · allgemein ohne Verfahren
4. Nur wenn unklar: welches Projekt genau bzw. welche Referenznummer.

Danach ohne weitere Rückfragen durcharbeiten.

## Schritt 2 – Fakten sammeln (nichts erfinden)

Quellen in dieser Reihenfolge:
1. **Referenzdatenbank** `N:\13. VGV\7-Referenzdatenbank\projekte\<id>.md` (Projekt über `INDEX.md`/`aliases.yaml` finden). Frontmatter = Stammwerte; `konflikte:` beachten; `themen:` zeigt, ob ein Fokus belegt ist (z. B. `holzbau`).
2. **Bisherige Darstellungen**: `referenz-instanzen\*__<id>.md` und vorhandene InDesign-ODs (`quellen.od_pdf`) – wie das Projekt früher zugeschnitten wurde.
3. **Projektordner** für fehlende oder neuere Werte (Verträge, Kostenberechnung/-feststellung, Flächenberechnung, Abnahmeprotokolle): `N:\1. Projekte\<Jahr>\…` und – bei neueren Projekten meist dort – `%USERPROFILE%\OneDrive - Gutthann HIW Architekten GmbH\_ <Jahr> - Dokumente\<Projektnr> <Name>` (SharePoint-Synchronisierung).
   Außerdem früher erarbeitete Referenzdaten in Verfahrensordnern: `N:\13. VGV\**\5-Analyse\*Referenzdaten*<Projekt>*.md` – enthalten oft schon belegte Werte mit Quelle, auch je Bauabschnitt.
4. **Bilder**: `N:\3. Marketing\1-Bilder\01_Hochbau\<Kategorie>\…` (Fotos, `02_Visuals` für Lagepläne/Grundrisse) und `N:\3. Marketing\2-Doku\…` (Ansichten, Schnitte als PDF → `#Seitennummer`). Marketing-Bilder zuerst; Fotodokus der Bauleitung im Projektordner nur, wenn dort nichts Passendes liegt – Urheber dann als `[zu ergänzen]` markieren.
5. **Bei Verfahren**: Bewertungsmatrix/Teilnahmeunterlagen im Verfahrensordner → die Kriterien für die Tabelle auf Seite 2 wörtlich übernehmen.

Regeln:
- Jeder Wert braucht eine Quelle. Kein Beleg → `<span class="offen">[zu ergänzen – wo es stehen müsste]</span>`. Nie schätzen, nie runden über die Quelle hinaus.
- Kostenangaben immer mit Kostenstand und Art (Kostenberechnung/-feststellung, brutto/netto, KG). Mio. € auf zwei Nachkommastellen ist erlaubt (3.285.629 € → 3,29 Mio. €); Stand = Datum im Dokument, sonst Dateidatum mit Vermerk.
- Widersprechen sich Quellen (Adresse, LPH, Flächen): neueste datierte Quelle gewinnt, bei Gleichstand das OD-Blatt; die Abweichung in der Antwort unter „bitte prüfen“ nennen.
- Bauabschnitte: Hat das Projekt mehrere BA, gilt der Abschnitt, den Datenbank-Datensatz bzw. vorhandene ODs als Referenz führen; Kennzahlen nie zwischen Abschnitten mischen, den Abschnitt im Titel oder `<small>` nennen.
- Ansprechpartner nur aus Datenbank/Projektunterlagen; private Kontaktdaten nie.
- ARGE-Projekte gelten als vollwertige eigene Referenzen (Rolle sichtbar nennen, nicht nachfragen).

## Schritt 3 – Auf den Fokus zuschneiden

Der Fokus ändert **Auswahl und Reihenfolge**, nie Fakten:
- **Titel bleibt der echte Projekttitel.** Fokus erscheint im Kicker, nur wenn belegt.
- **Kurzbeschreibung**: Fokus im ersten Satz, mit belegten Details (z. B. Holzbau: Konstruktion, Bauteile, Vorfertigung, Brandschutz, Holzart – nur was in den Quellen steht). Kernaussagen **fett**.
- **Projektdaten**: eine Fokus-Zeile ergänzen (z. B. „Bauweise: Holzhybrid – Tragwerk Stahlbeton, Fassade und Dach in Holz“).
- **Bilder**: zuerst die, die den Fokus zeigen (Holzfassade, Montage, Innenraum Holz).
- **Seite 2/3**: Kriterien bzw. Abschnitt „Bezug zur Aufgabe …“ auf den Fokus ausrichten.
- **Ist der Fokus nur teilweise belegt** (z. B. Holzfassade, aber Tragwerk Stahlbeton): mit Fokus bauen, die Grenze im Blatt genau benennen („Bauweise: Stahlbeton, Fassade in Holz“) und in der Antwort sagen, für welche Anforderung es reicht und für welche nicht; Dateiname mit dem tatsächlich belegten Begriff (`_Holzfassade` statt `_Holzbau`).
- **Ist der Fokus im Projekt nicht belegt** (z. B. kein `holzbau` in `themen`, nichts in den Unterlagen): Blatt trotzdem sauber ohne Fokus bauen und das in der Antwort klar sagen – „Projekt X ist kein Holzbau-Projekt, für eine Holzbau-Bewerbung eignen sich eher: …“ (2–3 Kandidaten mit `themen: holzbau` aus der Datenbank). Nie Holz erfinden.

## Schritt 4 – Blatt füllen

1. `vorlage.html` kopieren nach `<zielordner>\<dateiname>_entwurf.html`.
2. Nicht gebrauchte Seiten (`<section class="page">…</section>`) vollständig löschen; „Seite X von N“ anpassen.
3. Alle `{{…}}` ersetzen – außer `{{TITEL_KURZ}}` und `{{DATEINAME}}`, die setzt bauen.py. Der Anleitungskommentar oben darf stehen bleiben. Zeilen ohne Inhalt (z. B. Förderung) löschen statt leer lassen.
4. Positionen, Größen und CSS **nicht anfassen**. Zu viel Text → kürzen, nicht verkleinern. Erlaubt ist je Bild `data-fit0`/`data-fit` (`cover` für Fotos, `contain` + weißer Grund für Pläne) – z. B. Foto statt Lageplan, wenn kein Lageplan existiert.
5. Ohne Verfahren: Kicker „Projektreferenz“ (statt „Referenz N“), Fußzeile links „Gutthann HIW Architekten GmbH · Projektreferenz“, rechts nur „Seite X von N“; Überschrift Seite 2 „Schwerpunkt <Fokus>“, ohne Fokus „Projektmerkmale“ (Kriterien z. B. Art der Durchführung, Schwierigkeit, Leistungsumfang, Größenordnung, Termine, Besonderheiten). Fokus gehört in den Kicker („Projektreferenz · Holzbau“), nicht in den Titel – der Titelkasten fasst zwei Zeilen.
6. Textmengen als Richtwert: Kurzbeschreibung 600–1.000 Zeichen; Projektdaten max. ~15 Zeilen; Kriterien-Nachweise je 1–3 Zeilen.

Dateiname: `JJJJ-MM-TT_Projektdoku_<Verfahren-kurz>_Ref<N>_<Projekt-kurz>` – ohne Verfahren `JJJJ-MM-TT_Referenzblatt_<Projekt-kurz>[_<Fokus>]`.
Zielordner: bei Verfahren `<Verfahren>\2-Phase_1\2-Teilnahmeunterlagen_Anlagen\`, sonst der aktuelle Arbeitsordner.

## Schritt 5 – Bauen und prüfen (Pflicht)

```bash
python "<dieser Skill-Ordner>/bauen.py" "<zielordner>/<dateiname>_entwurf.html"
```

Das Skript setzt Logo und Bilder ein, druckt das PDF über Edge und prüft: keine Platzhalter, alle Bilder gefunden,
kein Textüberlauf, PDF-Seitenzahl = Blattseiten. **Erst bei „Alle Prüfungen grün.“ ist das Blatt fertig.**
Bei „NICHT FERTIG“: Ursache beheben (Text kürzen, Bildpfad korrigieren), erneut bauen. Danach den `_entwurf` löschen.
Braucht Python mit `Pillow` und `PyMuPDF` (`pip install pillow pymupdf`).

Dann das PDF mit dem Read-Werkzeug ansehen (Seite 1 mindestens) – sieht es aus wie das Muster?

## Umbau eines bestehenden Blatts („bau die Referenz um für Holzbau“)

1. Bestehendes Blatt (HTML) finden; nur Rückfragen stellen, die offen sind (meist: Seitenzahl gleich lassen?).
2. Inhalt aus dem HTML lesen (`#doc`), Bilder-Pfade aus `data-src` übernehmen.
3. Fakten für den neuen Fokus wie in Schritt 2 nachrecherchieren, Schritt 3 anwenden.
4. Neues Blatt aus `vorlage.html` aufbauen (nicht das alte überschreiben), neuer Dateiname mit Fokus, Schritt 5.
5. In der Antwort nennen, was sich gegenüber dem alten Blatt geändert hat (Texte, Bilder, Kriterien).

## Antwort an die Nutzerin

Kurz: wo HTML und PDF liegen, wie viele Werte `[zu ergänzen]` offen sind und welche (Liste), ob der Fokus belegt war.
Hinweis: Das HTML lässt sich im Browser mit **✎ Bearbeiten** direkt ändern (Text, Bilder tauschen/zoomen) und über **Drucken / PDF** neu ausgeben.
