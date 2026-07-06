# VGV-Analyse Skill - Automatische Ausfuehrung

> **ANWEISUNG:** Wenn du diese Datei liest, fuehre die komplette VGV-Analyse automatisch aus.
> Es ist KEIN weiterer Prompt noetig. Starte sofort mit Schritt 0.

---

## SCHRITT 0: Konfiguration laden (PFLICHT vor allem anderen)

### 0a. buero.json lesen
- Lies die Datei `buero.json` im aktuellen Skill-Ordner
- Extrahiere alle Konfigurationswerte: Bueroname, Logo, Rolle/Leistungsbild, CAD-System, Adresse, Farben etc.
- Diese Werte werden im gesamten Analyse-Prozess als Variablen verwendet

### 0b. Falls buero.json fehlt
Wenn keine `buero.json` existiert:
1. Lege eine `buero.json` an, indem du den Nutzer interaktiv abfragst:
   - Bueroname
   - Leistungsbild (Architekturbuero / Bauingenieurbuero / Generalplaner / Innenarchitektur / Landschaftsarchitektur / Andere)
   - Buerogroesse (Solo / 2-5 / 6-20 / >20 Personen)
   - Adresse
   - Logo-Pfad (Pfad zu einer Datei im `assets/`-Ordner)
   - CAD-System (Allplan / Archicad / Revit / Vectorworks / Andere)
   - Angebotene Leistungsphasen (LPH 1-9)
2. Speichere die Antworten in `buero.json`
3. Fahre erst dann mit Schritt 0c fort

### 0c. Profil laden (auf Basis Leistungsbild)
Lade ZUSAETZLICH zu dieser CLAUDE.md das passende Rollen-Profil aus `profiles/`:

| Leistungsbild in buero.json | Zu ladendes Profil |
|---|---|
| `Architekturbuero` | `profiles/architekt.md` |
| `Generalplaner` | `profiles/generalplaner.md` |
| `Bauingenieurbuero` | `profiles/bauingenieur.md` |

Diese drei Rollen sind in V1 vollstaendig ausgearbeitet und produktionsreif. Weitere Rollen (Innenarchitektur, Landschaftsarchitektur, Generalunternehmer etc.) werden in spaeteren Releases ergaenzt.

Falls in der `buero.json` ein anderes Leistungsbild steht, frage den Nutzer:
- "Diese Rolle ist in V1 noch nicht abgedeckt. Soll ich die Analyse generisch (ohne rollenspezifisches Profil) durchfuehren? [ja/nein]"
- Bei `ja`: Analyse ohne Profil-Laden durchfuehren, im Bericht hinweisen dass kein Rollenprofil verwendet wurde
- Bei `nein`: Abbruch mit Hinweis auf Skillboard fuer Updates

Das Profil enthaelt rollenspezifische Anweisungen (Honorarordnung, Vertragstyp, Pflichtnachweise, typische Risiken). Behandle alle Anweisungen im Profil als ERGAENZUNG/SPEZIFIZIERUNG zu dieser CLAUDE.md.

**Wichtig bei Bauingenieurbuero:** Das Profil `bauingenieur.md` enthaelt einen SCHRITT 0a, der die Fachdisziplin abfragt (Tragwerk / TGA / Bauphysik / Brandschutz / Tiefbau-Verkehr / Geotechnik-Vermessung). Diese Disziplin muss in `buero.json` unter `buero.fachdisziplin` gespeichert werden, bevor die Analyse startet.

### 0d. Variablen-Konvention
Ueberall in dieser Anweisung und in den Profilen werden Variablen aus `buero.json` mit `{{...}}` referenziert:
- `{{buero.name}}` - Name des Bueros (z.B. "Mustermann Architekten")
- `{{buero.logo_pfad}}` - Pfad zur Logo-Datei
- `{{buero.leistungsbild}}` - Rolle
- `{{buero.cad_system}}` - CAD-System
- `{{buero.adresse}}` - Anschrift
- `{{buero.primary_color}}` - Primaerfarbe (Deckblatt-Hintergrund, default #000000)
- `{{buero.secondary_color}}` - Sekundaerfarbe (Deckblatt-Text, default #FFFFFF)

Beim Erzeugen der HTML-Analyse werden diese Platzhalter durch die tatsaechlichen Werte ersetzt.

---

## WAS DU TUST

Du erstellst eine professionelle interne Vertragsrisiko- und VGV-Bewertung fuer `{{buero.name}}`.
Das Ergebnis sind bis zu drei HTML-Dateien im Ordner `5 Analyse/` des aktuellen Projekts:
Hauptanalyse, Referenz_Analyse (falls Referenzdatenbank konfiguriert) und TERMINE.html (siehe Schritt 10).
Den Ordner `5 Analyse/` legst du SOFORT bei Arbeitsbeginn an, falls er nicht existiert.
Qualitaetsniveau: Big-4-Beratung.

---

## SCHRITT 1: Vollstaendige Bestandsaufnahme

### 1a. Ordner scannen
- Scanne den GESAMTEN Projektordner rekursiv (alle Unterordner)
- Liste JEDE Datei auf: PDF, DOCX, DOC, XLSX, XLS, ZIP, PPTX, MSG, TXT
- Entpacke ZIP-Archive und scanne deren Inhalt
- Dokumentiere die Ordnerstruktur

### 1b. JEDE Datei lesen
- Lies JEDE EINZELNE SEITE von JEDEM Dokument
- Ueberspringe KEINE Dateien, auch wenn der Dateiname unwichtig erscheint
- Bei Word-Dateien: python-docx verwenden zum Extrahieren
- WICHTIG: Informationen koennen UEBERALL versteckt sein - in Fussnoten, Anlagen, Konzeptstudien, Machbarkeitsstudien

### 1b-KRITISCH: Machbarkeitsstudien und grosse PDFs - PFLICHTANWEISUNG

> **ACHTUNG - DIESE ANWEISUNG HAT HOECHSTE PRIORITAET:**
> Machbarkeitsstudien, Konzeptstudien und Vorstudien sind oft sehr grosse PDF-Dateien (50-200+ Seiten).
> Du darfst diese Dateien NIEMALS ueberspringen, abkuerzen oder nur teilweise lesen.
> Der Inhalt dieser Studien ist fuer die Analyse von ENORMER WICHTIGKEIT.

**Vorgehen bei grossen PDFs (>20 Seiten):**

1. **Seitenanzahl ermitteln:** Zuerst die Gesamtseitenzahl feststellen
2. **In Abschnitten lesen:** Lies das Dokument in Bloecken von max. 20 Seiten (z.B. Seiten 1-20, dann 21-40, dann 41-60 usw.)
3. **JEDEN Block vollstaendig verarbeiten:** Fasse die Kerninfos jedes Blocks zusammen BEVOR du zum naechsten weitergehst
4. **NICHTS ueberspringen:** Auch wenn Seiten nur Plaene, Tabellen oder Grafiken enthalten - beschreibe was du siehst
5. **Bei technischen Problemen:** Falls das Read-Tool bei einer bestimmten Seite scheitert, versuche es mit PyMuPDF:
   ```
   python3 -m pip install PyMuPDF
   ```
   Dann Seiten als Bilder rendern und visuell lesen. NIEMALS aufgeben und zur naechsten Datei springen.
6. **Fortschritt dokumentieren:** Melde dem Nutzer: "Machbarkeitsstudie Seite X von Y gelesen..."

**Was du aus Machbarkeitsstudien extrahieren MUSST:**
- Verfasser / Ersteller-Buero (Name, Ort)
- Datum der Studie
- Untersuchte Varianten und deren Bewertung
- Raumprogramm / Flaechenbedarfe
- Kostenangaben (KG 300/400, Gesamtkosten, Kostenkennwerte)
- Bestandsanalyse und dokumentierte Maengel
- Empfohlene Variante / Vorzugsvariante
- Technische Randbedingungen (Baugrund, Statik, Brandschutz, Energie)
- Zeitplaene / Terminvorstellungen
- Plaene und deren Inhalte (Lageplaene, Grundrisse, Schnitte)
- Foerdermittel-Hinweise
- Jede andere Information die fuer die VGV-Bewerbung relevant sein koennte

**VERBOTEN:**
- "Die Datei ist zu gross, ich ueberspringe sie" - VERBOTEN
- "Ich lese nur die ersten Seiten" - VERBOTEN
- "Die restlichen Seiten enthalten nur Plaene" - VERBOTEN (Plaene beschreiben!)
- "Ich fasse die Studie kurz zusammen" ohne sie vollstaendig gelesen zu haben - VERBOTEN

### 1c. Versteckte Informationen aktiv suchen
- Wer hat Vorstudien/Konzeptstudien/Machbarkeitsstudien erstellt? (Name des Bueros)
- Gibt es Bieterfragen-Dokumente?
- Gibt es eine Bewertungsmatrix / Gewichtungsmatrix?
- Gibt es Kostenangaben in den Studien?
- Gibt es Raumprogramme, Flaechenberechnungen?
- Gibt es Bestandsplaene, Gutachten?

---

## SCHRITT 2: Verfahrenstyp identifizieren (VORGESCHALTET)

Bevor du irgendetwas anderes analysierst, klaere:

1. **Verfahrensart:** Verhandlungsverfahren mit TNW? Offenes Verfahren? Nichtoffenes Verfahren? Wettbewerb?
2. **Generalplaner-VGV?** Werden GP-Leistungen gefordert (mehrere Fachdisziplinen wie TGA, Tragwerk, Freianlagen im Leistungsumfang)?
   - Falls JA: PROMINENT markieren - "GP-REFERENZEN ERFORDERLICH"
   - Falls NEIN: Nur Einzelplanung = Standard
   - Profilspezifische Bewertung steht im jeweiligen Rollen-Profil
3. **Leistungsumfang:** Welche Leistungsphasen? Welche Gewerke?
4. **Teilnehmeranzahl:** Wie viele werden eingeladen?

---

## SCHRITT 3: Terminuebersicht (ZENTRAL, ganz oben)

Suche ALLE Termine und Fristen aus ALLEN Dokumenten und stelle sie zentral zusammen:

- Bewerbungsfrist / Abgabefrist Teilnahmeantrag
- Frist fuer Bieterfragen
- Angebotsabgabefrist (Phase 2)
- Verhandlungsgespraech / Praesentation (Datum, Uhrzeit, Ort)
- Zuschlagsfrist
- Geplanter Leistungsbeginn
- Baubeginn / Fertigstellung
- Sonstige Fristen (Versicherungsnachweis, Unterlagennachreichung etc.)

Berechne: Wie viele Tage bis zur naechsten Frist?

Diese Terminuebersicht erscheint in der Hauptanalyse UND ist die Datenbasis fuer die separate `TERMINE.html` (siehe Schritt 10c).

---

## SCHRITT 4: Referenzanalyse (DETAILLIERT)

### 4a. Gewichtungsmatrix finden und auswerten
- Suche in ALLEN Dokumenten nach: Bewertungsmatrix, Gewichtungsmatrix, Eignungskriterien, Zuschlagskriterien
- Extrahiere die EXAKTE Punkteverteilung
- Unterscheide: Eignungskriterien (Phase 1) vs. Zuschlagskriterien (Phase 2)

### 4b. Referenzanforderungen - Mindest- vs. Bonuskriterien
Fuer JEDE geforderte Referenz:

**Mindestkriterien (KO-Kriterien - muessen erfuellt sein):**
- Projektart / Nutzung
- Honorarzone / Schwierigkeitsgrad
- Mindest-Leistungsphasen (welche LPH selbst erbracht?)
- Mindest-Baukosten (KG 300/400, brutto/netto?)
- Maximales Alter / Abschlussdatum
- Sonstige Mindestanforderungen

**Bonuskriterien (bringen Zusatzpunkte):**
- Spezielle Bauart (Holzbau, Passivhaus, Denkmal etc.)
- Spezielle Nutzung (Schulbau, Bauen fuer Kinder etc.)
- Spezielle Eigenschaften (Umbau, Erweiterung, Neubau)
- Oeffentlicher Auftraggeber

**Punktesystem:**
- Wie viele Punkte pro Kriterium?
- Wie ist die Gewichtung?
- Wo koennen Punkte geholt werden, auch bei Schwaeche in einem Bereich?

> **Hinweis:** Rollenspezifische Referenz-Anforderungen (z.B. welche HOAI-Paragraphen, welche Anlagengruppen bei TGA, welche Bauleistungen bei GU) stehen im jeweiligen Rollen-Profil.

### 4c. Anzahl und Spezifik
- Wie viele Referenzen muessen eingereicht werden?
- Wie viele KOENNEN eingereicht werden (Maximum)?
- Hat jede Referenz UNTERSCHIEDLICHE spezifische Anforderungen?
- Gibt es Referenzen fuer bestimmte Schluesselpersonen (PL, Bauleitung)?

### 4d. Eignungsleihe
- Ist Eignungsleihe moeglich/erwaehnt?
- Bewerbergemeinschaften zulaessig?

### 4e. Referenz-Matching aus der Referenzdatenbank (falls konfiguriert)

**Voraussetzung:** In `buero.json` ist das Feld `buero.referenzdatenbank` gesetzt (Pfad zu einer buero-weiten Referenzdatenbank).

- Falls das Feld fehlt: frage den Nutzer einmalig "Gibt es eine buero-weite Referenzdatenbank? Falls ja, Pfad angeben - falls nein, 'nein'." Speichere die Antwort in `buero.json` (`referenzdatenbank: "<pfad>"` oder `null`), damit die Frage nie wieder kommt.
- Falls `null` oder der Pfad nicht erreichbar ist (z.B. Netzlaufwerk nicht verbunden): Schritt ueberspringen, in der HTML-Analyse kurz vermerken ("Referenz-Matching uebersprungen - keine Referenzdatenbank verfuegbar").
- **Die Referenzdatenbank ist strikt read-only.** Du schreibst dort NIEMALS hinein.

**Datenbank lesen (in dieser Reihenfolge):**
1. `SCHEMA.md` und `INDEX.md` im Datenbank-Ordner lesen. SCHEMA.md definiert Felder und kontrollierte Vokabulare - verlass dich auf SCHEMA.md, nicht auf Annahmen aus dieser Anleitung, die Struktur kann sich weiterentwickeln.
2. Kandidaten-Suche per Grep ueber `projekte\*.md` (YAML-Frontmatter: gebaeudekategorie, leistungsart, themen, kostenklasse, lph_umfang, ag_typ, Flaechen, Kosten, Termine).
3. Fuer die Kandidaten: `referenz-instanzen\` lesen (wie wurde das Projekt in frueheren Verfahren positioniert) und `verfahren\` (mit welchem Ausgang: zusage/absage/praesentation).
4. Falls die Datenbank erst teilweise aufgebaut ist (z.B. `referenz-instanzen\` noch leer): mit `projekte\*.md` arbeiten und im Bericht vermerken, dass die Anpassungshistorie noch nicht verfuegbar ist.

**Matching-Agent starten:**
Starte einen Subagenten (Task-Tool) mit einem in sich vollstaendigen Auftrag. Falls Subagenten nicht verfuegbar sind, fuehre das Matching direkt aus. Der Auftrag enthaelt:
- Die in 4b extrahierten Referenzanforderungen (Mindest- und Bonuskriterien, Punktesystem, Anzahl geforderter Referenzen, ggf. unterschiedliche Anforderungen je Referenz)
- Den Projektsteckbrief des neuen Verfahrens (aus Schritt 5): Bauaufgabe, Nutzung, Kostenrahmen, LPH-Umfang, AG-Typ, Besonderheiten
- Den Pfad zur Referenzdatenbank und die Verhaltensregeln unten

**Verhalten des Matching-Agents (VERBINDLICH):**

Architekten und Projektleiter legen Referenzen fuer ein neues Verfahren "zurecht" - sie waehlen aus und betonen, was zum Verfahren passt. Der Agent bildet genau dieses Verhalten ab, aber ausschliesslich innerhalb der dokumentierten Fakten:

**ERLAUBT (Zuschnitt):**
- Projekt-Bezeichnung auf das Verfahren zuschneiden (z.B. "Generalsanierung und Erweiterung Grundschule X bei laufendem Betrieb" statt internem Kurznamen) - solange faktentreu
- Auswahl, WELCHE der tatsaechlich erbrachten Leistungsphasen dargestellt werden (dargestellte LPH muessen eine Teilmenge der erbrachten LPH sein)
- Wahl der dokumentierten Kostenbasis (KG 300+400 vs. Gesamtkosten KG 200-700), passend zu dem, was das Verfahren abfragt - die gewaehlte Basis im Vorschlag immer ausweisen
- Narrative Betonung real vorhandener Eigenschaften (Denkmal, laufender Betrieb, Foerderprogramm, Holzbau, Barrierefreiheit ...) je nach Bonuskriterien des Verfahrens
- Honorarzone/Schwierigkeitsgrad wie in den Stammdaten dokumentiert; eine begruendbare abweichende Einstufung nur als gekennzeichneter Vorschlag ("abweichend von Stammdaten, Begruendung: ...")
- Wiederverwendung erprobter Zuschnitte aus `referenz-instanzen\` - bevorzugt solche aus gewonnenen Verfahren (ausgang=zusage)

**VERBOTEN (Faktenaenderung):**
- Zahlen aendern oder erfinden (Baukosten, Flaechen, Termine)
- Leistungsphasen behaupten, die nicht erbracht wurden
- Fertigstellungsdaten in den geforderten Referenzzeitraum "verschieben"
- Eigenschaften, Themen oder Nutzungen erfinden, die das Projekt nicht hat
- Bauherr, Vertragsrolle (allein vs. ARGE vs. Nachunternehmer) oder Auftragsverhaeltnis umdeuten

**GRENZFAELLE - markieren statt entscheiden:**
Faelle wie: Fertigstellung knapp ausserhalb des Referenzzeitraums, Baukosten knapp unter der Mindestgrenze, unklarer eigener LPH-Anteil (ARGE), Nutzung nur teilweise passend. Solche Kandidaten trotzdem listen, aber deutlich kennzeichnen: **"(Grenzfall - Ruecksprache Projektleitung)"** mit einem Satz Begruendung. Der Agent trifft hier KEINE Entscheidung.

**Belegpflicht:** Jede Angabe im Vorschlag muss auf ein Feld der Datenbank oder ein dort verlinktes Quelldokument zurueckfuehrbar sein (Quellpfad nennen). Luecken als `(Verifikation noetig)` markieren.

**Ranking-Logik:**
1. Hard-Filter: Mindestkriterien (KO) gegen die WAHREN Stammdaten pruefen - nicht mit dem Zuschnitt schoenrechnen
2. Punkte-Schaetzung je Bonuskriterium anhand des Punktesystems aus 4a/4b
3. Bonus fuer: frueher in gewonnenen Verfahren verwendet (ausgang=zusage), Referenzschreiben vorhanden, gleicher AG-Typ, regionale Naehe
4. Output je geforderter Referenz: 3-5 Kandidaten als Rangliste mit:
   - Erfuellungsmatrix (je Mindest-/Bonuskriterium: erfuellt / Grenzfall / nicht erfuellt)
   - Punkteschaetzung
   - Empfohlener Zuschnitt: Bezeichnung, darzustellende LPH, Kostenbasis, Kernnarrativ (2-3 Saetze)
   - Nachweise: Referenzschreiben vorhanden ja/nein + Pfad
   - Fruehere Verwendung: in welchen Verfahren, mit welchem Ausgang

Das Ergebnis wird in die SEPARATE Datei `Referenz_Analyse_{YYYY-MM-DD}.html` geschrieben (Schritt 10b), NICHT in die Hauptanalyse.

---

## SCHRITT 5: Projektanalyse aus allen Quellen

### 5a. Projektdaten
- Bauaufgabe, Nutzung, Standort
- Baukosten (KG 300/400 netto UND brutto)
- Projektlaufzeit, Bauzeit
- Regierungsbezirk / Region identifizieren

### 5b. Vorstudien auswerten
- Wer hat die Konzeptstudie erstellt? (Bueroname!)
- Wer hat die Machbarkeitsstudie erstellt?
- Raumprogramm, Flaechenberechnungen extrahieren
- Bestandsmaengel dokumentieren
- Varianten/Optionen zusammenfassen
- Kostenangaben aus den Studien

### 5c. Bestandssituation (bei Umbau/Erweiterung)
- Vorhandene Bestandsunterlagen?
- Gutachten vorhanden? (Baugrund, Schadstoffe, Brandschutz, Energie)
- Baujahr, Zustand, bekannte Maengel
- Denkmalschutz?

### 5d. Besondere Herausforderungen
- Bauen bei laufendem Betrieb?
- Foerdermittel? Welches Programm?
- Wirtschaftlichkeitsprioritaet?
- Oertliche Praesenz gefordert?

---

## SCHRITT 6: Vertragsanalyse (INTELLIGENT GEFILTERT)

> **Wichtig:** Welcher Vertragstyp typisch ist (HAV-KOM bei Architekt, RBBau bei Ingenieur, VOB-Werkvertrag bei GU etc.) ist im jeweiligen Rollen-Profil beschrieben. Folge dort den Anweisungen fuer die rollenspezifischen Prueffragen.

### 6a. Vertragsmuster identifizieren
- Ist es ein Standard-Mustervertrag der oeffentlichen Hand? Welche Fassung?
- Ist es ein individueller Vertrag?
- Sind AVB/ZVB Standardfassungen oder modifiziert?

### 6b. Bei Standardvertrag: NUR Kritisches
Wenn es ein unveraenderter Mustervertrag ist: NICHT jede einzelne Standard-AVB-Klausel analysieren.
Stattdessen:
- **Platzhalter/LEER-Felder:** Alle offenen Felder identifizieren (Kostenobergrenze, Honorarzone, Umbauzuschlag, Stundensaetze, Nebenkosten, Deckungssummen, Termine)
- **Abweichungen vom Standard:** Nur Klauseln die vom Standard ABWEICHEN
- **Verbindliche Kostenobergrenze:** Ist sie schon festgelegt oder wird sie erst spaeter definiert?
- **Gesamtbewertung:** "Vertrag kann unterschrieben werden" oder "Vertrag hat problematische Klauseln"

### 6c. Bei individuellem Vertrag: Tiefenanalyse
Jede Klausel einzeln nach dem Schema:
- Paragraphen-Referenz und Wortlaut-Zusammenfassung
- Was bedeutet das KONKRET fuer den AN? Worst-Case-Szenario?
- Risikostufe: HOCH / MITTEL / ZUR KENNTNIS
- Konkrete Handlungsempfehlung mit Sofortmassnahmen

### 6d. Immer analysieren (ob Standard oder nicht):
- Kostenobergrenze und deren Konsequenzen
- Stufenweise Beauftragung und Folgestufen-Anspruch
- Honorarparameter die noch verhandelt werden
- Kuendigungsregelungen die vom Standard abweichen
- Haftung die ueber Standard hinausgeht

---

## SCHRITT 7: Bieterfragen identifizieren

- Bereits gestellte Bieterfragen zusammenfassen
- Unklarheiten identifizieren die geklaert werden muessen
- Fuer jede Unklarheit: Konkreten Fragetext formulieren

---

## SCHRITT 8: Risikoanalyse und Empfehlung

### Risikouebersicht-Tabelle
Alle identifizierten Risiken in EINER Tabelle, sortiert nach Risikostufe.

### Gesamtbewertung
- Risikostufe: HOCH / MITTEL / NIEDRIG
- Empfehlung: Bewerben JA/NEIN/UNTER BEDINGUNGEN

### Checkliste vor Vertragsunterzeichnung
Nummerierte Liste aller Punkte die VOR Unterschrift abgearbeitet sein muessen.

---

## SCHRITT 9: Detaillierter Punkt-fuer-Punkt-Plan bis Teilnahmeerklaerung

Erstelle eine VOLLSTAENDIGE, nummerierte Checkliste aller Dokumente und Dateien, die fuer eine erfolgreiche Teilnahmeerklaerung erstellt/beschafft werden muessen. Diese Liste ist das zentrale Arbeitsdokument fuer das Team.

### 9a. Dokumente aus den VGV-Unterlagen ableiten
Lies die Teilnahmeunterlagen / Aufforderung zur Interessensbestaetigung / Bekanntmachung und extrahiere JEDES EINZELNE geforderte Dokument:

**Formale Unterlagen:**
- Teilnahmeantrag / Bewerbungsbogen (ausgefuellt)
- Eigenerklaerungen (welche genau? Antikorruption, Scientology, Mindestlohn etc.)
- Verpflichtungserklaerungen (welche?)
- Handelsregisterauszug / Gewerbeanmeldung
- Nachweis Berufshaftpflichtversicherung (geforderte Deckungssummen!)
- Nachweis Berufszulassung / Kammermitgliedschaft (falls anwendbar - siehe Rollen-Profil)
- Umsatzerklaerungen (welche Jahre? Mindesthoehe?)

**Referenz-Dokumente (pro geforderte Referenz):**
- Referenzblaetter / Projektdatenblaetter (Format vorgegeben?)
- Referenzschreiben / Auftraggeber-Bestaetigung
- Bildmaterial / Plaene (Anzahl, Format, Aufloesung?)
- Angaben zu Baukosten, Flaechen, Leistungsphasen

**Personalbezogene Unterlagen:**
- Lebenslaeufe (PL, stv. PL, Bauleitung - welches Format?)
- Qualifikationsnachweise / Studiennachweise
- Personenreferenzen (welche Anforderungen pro Person?)

**Bei Generalplaner-VGV zusaetzlich:**
- Nachweise fuer jedes Fachplanungsbuero
- Verpflichtungserklaerungen der Nachunternehmer
- Eignungsleihe-Vereinbarungen (falls zutreffend)

**Sonstige:**
- Bietergemeinschaftserklaerung (falls zutreffend)
- Nachunternehmerverpflichtungserklaerung
- Datenschutzerklaerung
- Sonstige projektspezifische Nachweise

> **Rollenspezifische Pflichtnachweise** (z.B. Pruefingenieur-Nachweis bei Tragwerk, GU-Faehigkeitsnachweis bei Generalunternehmer) stehen im jeweiligen Rollen-Profil.

### 9b. Status-Checkliste erstellen
Fuer JEDES Dokument in der HTML-Analyse eine Zeile mit:
- [ ] Lfd. Nr.
- [ ] Dokumentenbezeichnung (exakt wie in den Unterlagen gefordert)
- [ ] Quelle / Fundstelle in den VGV-Unterlagen (Seitenzahl, Paragraph)
- [ ] Verantwortlich (wer muss es erstellen/beschaffen?)
- [ ] Frist (bis wann muss es fertig sein - mit Puffer vor Abgabefrist)
- [ ] Hinweise (Mindestanforderungen, Formvorgaben, Besonderheiten)

### 9c. Reihenfolge und Abhaengigkeiten
- Welche Dokumente muessen ZUERST erstellt werden (weil andere darauf aufbauen)?
- Welche Dokumente koennen parallel erstellt werden?
- Welche Dokumente muessen von EXTERNEN beschafft werden (laengere Vorlaufzeit)?
- Vorgeschlagener Zeitplan mit Meilensteinen bis zur Abgabefrist

---

## SCHRITT 10: HTML-Outputs erstellen

Alle Output-Dateien landen im Ordner **`5 Analyse/`** im Projekt-Root. Diesen Ordner SOFORT bei Arbeitsbeginn anlegen, falls nicht vorhanden. Ausserhalb dieses Ordners wird NICHTS geschrieben.

Es entstehen bis zu drei Dateien:
- `VGV_Analyse_[Projektname]_[YYYY-MM-DD].html` (Hauptanalyse, immer - Schritt 10a)
- `Referenz_Analyse_[Projektname]_[YYYY-MM-DD].html` (nur falls Referenz-Matching gelaufen ist - Schritt 10b)
- `TERMINE.html` (immer - Schritt 10c)

### 10a. Hauptanalyse

Erstelle die Analyse als EINE HTML-Datei mit:

### Struktur:
1. Deckblatt (Branding aus buero.json - siehe Design-Anforderungen unten)
2. Terminuebersicht (ZENTRAL, alle Fristen auf einen Blick)
3. Inhaltsverzeichnis
4. Referenz- und Eignungsanalyse (mit Punktesystem und Gewichtung)
5. Projektanalyse (inkl. Vorstudien-Auswertung)
6. Vertragsanalyse (intelligent gefiltert)
7. Empfohlene Bieterfragen
8. Checkliste vor Vertragsunterzeichnung
9. Detaillierter Plan bis Teilnahmeerklaerung (Punkt-fuer-Punkt mit allen Dokumenten)
10. Zusammenfassung und Entscheidungsgrundlage
11. Anhang (Dokumentenuebersicht)

Direkt unter der Terminuebersicht: kleine Verweis-Box mit relativen Links auf `TERMINE.html` und (falls erstellt) `Referenz_Analyse_[...].html` - beide liegen im selben Ordner.

### Design-Anforderungen:

**Deckblatt (Seite 1) - Branding aus buero.json:**
- Hintergrund: `{{buero.primary_color}}` (Default `#000000`), vollflaechig
- Logo: Zentriert, gross und prominent platziert
- Logo-Quelle: `{{buero.logo_pfad}}` (typisch `assets/logo.png` im Skill-Ordner)
- Logo-Einbindung: Als Base64-encoded `<img>` Tag direkt in der HTML (damit die Datei standalone funktioniert)
- Text auf dem Deckblatt: `{{buero.secondary_color}}` (Default `#FFFFFF`) - Projektname, Auftraggeber, Verfahrenstyp, Datum, GP ja/nein
- Auf dem Deckblatt nur die zwei Brandingfarben verwenden
- Schriftart: Sans-serif, modern, clean (z.B. system-ui oder Arial)
- Falls kein Logo in buero.json hinterlegt ist: Bueroname `{{buero.name}}` als grosse Textmarke statt Logo verwenden

**Alle weiteren Seiten (ab Seite 2):**
- Weisser Hintergrund mit Warn-/Signalfarben:
  - Rot (`#DC3545`) = HOCH-Risiko
  - Orange (`#FD7E14`) = MITTEL-Risiko
  - Blau (`#0D6EFD`) = INFO / Zur Kenntnis
  - Gruen (`#198754`) = POSITIV / Erfuellt
- Logo klein in der Kopfzeile oder Fusszeile jeder Seite (optional, dezent)
- Professionelles Design auf Big-4-Niveau
- Sticky Filter-Toggle zum Ausblenden von Platzhalter-Risiken
- Risikouebersicht-Tabelle ganz oben (nach Deckblatt)
- Cards, Timeline, Risk Meter
- Druckbar (CSS @media print)
- Responsive

### Interaktive Buttons (fest in der HTML-Datei integriert):
- **PDF-Download-Button:** Oben rechts fixiert (sticky). Nutzt `window.print()` mit optimierten `@media print`-Styles fuer sauberen PDF-Export. Button-Text: "Als PDF herunterladen". Die Print-Styles muessen alle interaktiven Elemente (Buttons, Filter-Toggle) ausblenden und ein druckoptimiertes Layout erzeugen.
- **Bearbeitungs-Button:** Daneben platziert. Aktiviert einen Inline-Bearbeitungsmodus (`contenteditable="true"`) fuer alle Textbereiche der Analyse. Im Bearbeitungsmodus:
  - Button-Text wechselt zu "Bearbeitung beenden"
  - Bearbeitbare Bereiche erhalten einen sichtbaren Rahmen (z.B. gestrichelter blauer Rand)
  - Aenderungen werden im DOM live gespeichert (bleiben bis zum Neuladen erhalten)
  - Beim Beenden des Bearbeitungsmodus wird `contenteditable` wieder entfernt
- Beide Buttons muessen visuell zum Gesamtdesign passen (gleiche Farbpalette, abgerundete Ecken, Hover-Effekte)

### Dateiname:
`5 Analyse/VGV_Analyse_[Projektname]_[YYYY-MM-DD].html`

### 10b. Referenz_Analyse HTML (nur falls Referenzdatenbank konfiguriert)

Das Ergebnis des Referenz-Matchings (Schritt 4e) kommt NICHT in die Hauptanalyse, sondern in eine eigene Datei:

**Datei:** `5 Analyse/Referenz_Analyse_[Projektname]_[YYYY-MM-DD].html`

Struktur:
1. Deckblatt (gleiches Branding wie Hauptanalyse), Titel "Referenz-Empfehlungen", Verfahrensname, Datum
2. Zusammenfassung der Referenzanforderungen des Verfahrens (aus Schritt 4b): Mindest- und Bonuskriterien, Punktesystem, Anzahl geforderter Referenzen
3. Pro geforderter Referenz das Kandidaten-Ranking als Cards/Tabelle mit Ampel:
   - Erfuellungsmatrix (je Kriterium: erfuellt / Grenzfall / nicht erfuellt)
   - Punkteschaetzung
   - Empfohlener Zuschnitt (Bezeichnung, darzustellende LPH, Kostenbasis, Kernnarrativ)
   - Nachweise (Referenzschreiben ja/nein + Pfad)
   - Fruehere Verwendung (Verfahren + Ausgang)
   - Grenzfaelle deutlich als "(Grenzfall - Ruecksprache Projektleitung)" markiert
4. Hinweis-Box am Ende: angewandte Zuschnitt-Regeln (erlaubt vs. verboten) + Belegpflicht - damit jeder Leser weiss, dass keine Fakten veraendert wurden
5. Rueckverweis-Link auf die Hauptanalyse (relative Verlinkung, gleicher Ordner)

Design, PDF-Download-Button und Bearbeitungsmodus wie bei der Hauptanalyse.

### 10c. TERMINE.html (immer erstellen)

Alle Termine und Fristen aus Schritt 3 als eigene, schnell auffindbare Datei:

**Datei:** `5 Analyse/TERMINE.html` - FESTER Dateiname ohne Datum. Wird bei jedem Lauf komplett neu geschrieben (die einzige Datei, die ueberschrieben wird), damit das Team sie immer am selben Ort findet.

Struktur:
1. Kopf: Verfahrensname, Buero-Branding dezent, Stand-Datum ("Stand: YYYY-MM-DD")
2. **"Naechste Frist"-Box** prominent ganz oben: was, wann, verbleibende Tage
3. Chronologische Termintabelle: Datum | Uhrzeit | Termin/Frist | Quelle (Dokument + Seite/Abschnitt) | Anmerkung (z.B. "Ausschlussfrist!", "Puffer einplanen")
4. Visuelle Timeline aller Termine
5. Countdown-Angaben ("noch X Tage") per JavaScript beim Oeffnen live berechnen (`new Date()`), nicht statisch einbrennen - so stimmt die Datei auch Wochen spaeter noch
6. Vergangene Termine automatisch ausgegraut darstellen (ebenfalls per JavaScript)

Design wie Hauptanalyse (Cards, druckbar, PDF-Download-Button). Keine Termine erfinden - nur was in den Unterlagen steht, jeweils mit Quellenangabe.

### Ablageort (alle Dateien):
`5 Analyse/` im aktuellen Projektordner. Ordner bei Arbeitsbeginn anlegen falls nicht vorhanden.

---

## QUALITAETSSTANDARDS

- JEDE Klausel mit Paragraphen-Referenz
- KONKRETE Handlungsempfehlungen (nicht "pruefen", sondern "Tracker anlegen", "E-Mail mit Lesebestaetigung versenden")
- Worst-Case-Szenarien benennen
- Querverweise zwischen Klauseln zeigen
- Exakte Fristen und Betraege aus dem Vertrag
- Kein Schoenfaerben - jedes Risiko schonungslos benennen
- GP-VGV prominent markieren wenn zutreffend
- Ersteller von Vorstudien identifizieren und nennen
- Rollenspezifische Details aus dem geladenen Profil beruecksichtigen
