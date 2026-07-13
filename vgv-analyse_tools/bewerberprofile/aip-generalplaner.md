# Bewerberprofil: AIP Generalplanergesellschaft

> **Anwendung:** Wird geladen, wenn in `bewerbung.json` die Konstellation `aip` gesetzt ist.
> Bewerber ist NICHT `{{buero.name}}` selbst, sondern die AIP Generalplanergesellschaft.
> Dieses Suchprofil ergaenzt ANLEITUNG.md und das Rollen-Profil mit konstellationsspezifischen Pruefpunkten.

---

## Stammdaten der Gesellschaft (hier einmalig pflegen)

| Feld | Wert |
|---|---|
| Genaue Firmierung | (pflegen) |
| Rechtsform | (pflegen) |
| Sitz / Anschrift | (pflegen) |
| Gruendungsjahr | (pflegen) |
| Gesellschafter / beteiligte Bueros | (pflegen) |
| Eigene Berufshaftpflicht (Versicherer, Deckungssummen) | (pflegen) |
| Kammereintrag / bauvorlageberechtigte Person | (pflegen) |

Solange Felder auf "(pflegen)" stehen: Angaben, die fuer die konkrete Analyse gebraucht werden, beim Start miterfragen und in der `bewerbung.json` des Projekts speichern. Diese Profil-Datei wird waehrend eines Laufs NICHT automatisch beschrieben - Stammdaten pflegt der Nutzer hier von Hand.

---

## Zusatzfragen beim Start

1. "Wie heisst die Gesellschaft genau (Firmierung)?" - entfaellt, falls oben gepflegt; dann nur kurz bestaetigen
2. "Welche Bueros/Fachdisziplinen der Gesellschaft sind in diesem Verfahren beteiligt?"
3. Allgemeine Referenz-/Hinweis-Frage (ANLEITUNG.md Schritt 0e)

---

## Suchprofil - was in den Vergabeunterlagen zusaetzlich zu pruefen ist

### Bewerber-Identitaet
- ALLE Erklaerungen, Nachweise und Formblaetter lauten auf die Gesellschaft, nicht auf `{{buero.name}}`
- Mehrfachbeteiligung: `{{buero.name}}` und die anderen Gesellschafter-Bueros duerfen sich im selben Verfahren nicht zusaetzlich einzeln bewerben - Ausschlussregeln pruefen

### GP-Anforderungen und Fachdisziplinen
- Welche Fachdisziplinen fordert das Verfahren (Objektplanung, Tragwerk, TGA, Freianlagen, Brandschutz ...)?
- Deckt die Gesellschaft alle geforderten Disziplinen ab? Fehlende Disziplinen: Nachunternehmer (§ 36 VgV) noetig - als Aufgabe mit Verpflichtungserklaerung listen

### Referenzen - Kernfrage dieser Konstellation
- Was lassen die Bewerbungsbedingungen zu: Referenzen der GESELLSCHAFT selbst oder auch Referenzen der GESELLSCHAFTER-Bueros?
- Falls die Gesellschaft jung ist und eigene Referenzen fehlen: Eignungsleihe (§ 47 VgV) auf die Gesellschafter pruefen - ist sie im Verfahren zugelassen, welche Erklaerungen werden dafuer gefordert?
- Bei jeder vorgeschlagenen Referenz ausweisen, WER sie erbracht hat (Gesellschaft / Gesellschafter-Buero) und ob das Verfahren diese Zurechnung erlaubt - bei Unklarheit als Grenzfall markieren, Bieterfrage vorschlagen

### Wirtschaftliche Eignung
- Umsatzanforderungen (§ 45 VgV, meist letzte 3 Geschaeftsjahre): kann die Gesellschaft sie selbst erfuellen? Falls nicht (Neugruendung): Regelung fuer junge Unternehmen in den Unterlagen suchen, sonst Eignungsleihe/Bieterfrage
- Berufshaftpflicht: eigene Police der Gesellschaft oder projektbezogene Deckungszusage? Geforderte Deckungssummen gegen Stammdaten pruefen
- Berufszulassung/Kammer: wer in der Gesellschaft erfuellt die Anforderung (Kammereintrag, Bauvorlageberechtigung)?

### Nachweise (ANLEITUNG.md Schritt 9)
- Checkliste auf die Gesellschaft ausstellen; zusaetzlich je beteiligtem Buero die geforderten Einzel-Nachweise (Eigenerklaerungen, ggf. Verpflichtungserklaerungen)
- Verantwortlich-Spalte: je Dokument das zustaendige Gesellschafter-Buero benennen
- Dokumente anderer Bueros = externe Beschaffung: Frist mit Puffer VOR der Abgabefrist setzen

### Vertrag und Haftung
- Vertragspartner des AG ist die Gesellschaft - Haftungsklauseln aus Sicht der Gesellschaft bewerten
- Durchgriff/Innenhaftung haengt von der Rechtsform ab: nicht spekulieren, bei Relevanz "(Verifikation noetig - Rechtsform klaeren)" markieren

---

## Hinweise fuer die HTML-Analyse

- Deckblatt: Bewerber-Zeile "Bewerber: AIP Generalplanergesellschaft" (genaue Firmierung aus Stammdaten/bewerbung.json)
- In der Referenzanalyse je Referenz die Zurechnung (Gesellschaft vs. Gesellschafter) sichtbar machen
- In der Zusammenfassung die Konstellation und die beteiligten Bueros nennen
