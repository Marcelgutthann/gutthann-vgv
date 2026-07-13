# Bewerberprofil: ARGE / Bewerbergemeinschaft

> **Anwendung:** Wird geladen, wenn in `bewerbung.json` die Konstellation `arge` gesetzt ist.
> `{{buero.name}}` bewirbt sich gemeinsam mit einem Partner als Bewerbergemeinschaft (§ 43 VgV).
> "ARGE" ist die gaengige Kurzbezeichnung; vergaberechtlich heisst die Konstellation Bewerber- bzw. Bietergemeinschaft.
> Dieses Suchprofil ergaenzt ANLEITUNG.md und das Rollen-Profil mit konstellationsspezifischen Pruefpunkten.

---

## Zusatzfragen beim Start

1. "Wie heisst die andere Gesellschaft genau (Firmierung, Sitz)?" -> `{{bewerbung.partner}}`
2. "Wer ist bevollmaechtigter Vertreter der Bewerbergemeinschaft - `{{buero.name}}` oder der Partner? Und wie ist die Leistungsaufteilung grob geplant?"
3. Allgemeine Referenz-/Hinweis-Frage (ANLEITUNG.md Schritt 0e) - hier besonders wichtig: Referenzen, die der PARTNER beisteuern soll

---

## Suchprofil - was in den Vergabeunterlagen zusaetzlich zu pruefen ist

### Zulassung der Bewerbergemeinschaft
- Sind Bewerbergemeinschaften zugelassen? (§ 43 VgV - Bewerbungsbedingungen und Bekanntmachung pruefen; Einschraenkungen oder geforderte Begruendungen vermerken)
- Wird ein Formblatt "Bewerbergemeinschaftserklaerung" / "Bietergemeinschaftserklaerung" gefordert? Fundstelle und geforderten Inhalt notieren (Mitglieder, bevollmaechtigter Vertreter, gesamtschuldnerische Haftung)
- Mehrfachbeteiligungs-Verbot: darf ein Mitglied im selben Verfahren zusaetzlich als Einzelbewerber oder in anderer Gemeinschaft auftreten? Verstoss = Ausschlussrisiko - PROMINENT markieren und beide Mitglieder darauf hinweisen

### Referenzen - Kernfrage dieser Konstellation
- Duerfen BEIDE Mitglieder Referenzen beisteuern? Muss jede geforderte Referenz von EINEM Mitglied allein erfuellt sein oder duerfen Kriterien kumulativ erfuellt werden?
- Wie werden fruehere ARGE-Referenzen gewertet - zaehlt der eigene Leistungsanteil?
- Referenz-Matching (ANLEITUNG.md Schritt 4e): die Referenzdatenbank deckt nur `{{buero.name}}` ab. Partner-Referenzen NICHT erfinden - vom Nutzer genannte Partner-Referenzen (Hinweis-Frage) einbeziehen und als "(Angabe Nutzer - Verifikation noetig)" kennzeichnen; fehlende Partner-Referenzen als Aufgabe "vom Partner beizustellen" listen

### Eignungsnachweise je Mitglied
- Welche Nachweise muss JEDES Mitglied einzeln bringen (Eigenerklaerungen, Handelsregister, Berufshaftpflicht, Kammermitgliedschaft)?
- Umsatzanforderungen (§ 45 VgV): kumuliert ueber die Gemeinschaft oder Mindesthoehe je Mitglied?
- Berufshaftpflicht: je Mitglied eigene Police oder gemeinsame projektbezogene Deckung fuer die ARGE gefordert?

### Haftung und Innenverhaeltnis
- Gesamtschuldnerische Haftung der Mitglieder: als Risiko HOCH in die Risikouebersicht aufnehmen - jedes Mitglied haftet fuer Fehler des anderen
- Handlungsempfehlung: ARGE-internen Vertrag mit Haftungs- und Leistungsabgrenzung VOR Abgabe des Teilnahmeantrags aufsetzen (Hinweis: rechtliche Ausgestaltung durch Anwalt, kein Rechtsrat durch dieses Tool)

### Nachweise (ANLEITUNG.md Schritt 9)
- Checkliste je Dokument mit Verantwortlich-Spalte: `{{buero.name}}` oder `{{bewerbung.partner}}`
- Alle Partner-Dokumente = externe Beschaffung: laengere Vorlaufzeit, Frist mit Puffer deutlich VOR der Abgabefrist setzen und als Nachhak-Punkt markieren
- Bewerbergemeinschaftserklaerung mit Unterschriften BEIDER Mitglieder als eigener Checklisten-Punkt

---

## Hinweise fuer die HTML-Analyse

- Deckblatt: Bewerber-Zeile "Bewerbergemeinschaft (ARGE): `{{buero.name}}` + `{{bewerbung.partner}}`"
- In der Referenzanalyse je Referenz sichtbar machen, welches Mitglied sie einbringt
- In der Zusammenfassung die Konstellation, den bevollmaechtigten Vertreter und die Leistungsaufteilung nennen
