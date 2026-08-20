# Bewerberprofil: GHIW (Einzelbewerbung)

> **Anwendung:** Wird geladen, wenn in `bewerbung.json` die Konstellation `ghiw` gesetzt ist.
> Das Buero `{{buero.name}}` bewirbt sich ALLEIN als Einzelbewerber.
> Dieses Suchprofil ergaenzt ANLEITUNG.md und das Rollen-Profil mit konstellationsspezifischen Pruefpunkten.

---

## Konstellation

- Bewerber: `{{buero.name}}` als Einzelbewerber
- Keine weiteren Gesellschaften beteiligt
- **Zusatzfragen beim Start:** keine (nur die allgemeine Referenz-/Hinweis-Frage aus ANLEITUNG.md Schritt 0e)

---

## Suchprofil - was in den Vergabeunterlagen zusaetzlich zu pruefen ist

### Zulassung und Eignung
- Sind Einzelbewerber ohne Einschraenkung zugelassen? (Standard: ja - nur bei Abweichung vermerken)
- Werden GP-Leistungen oder mehrere Fachdisziplinen gefordert, die `{{buero.name}}` nicht selbst abdeckt?
  - Falls JA: PROMINENT als Risiko markieren - Einzelbewerbung nur mit Nachunternehmern (§ 36 VgV) oder Eignungsleihe (§ 47 VgV) machbar
  - Empfehlung im Bericht: Konstellation AIP Generalplanergesellschaft oder ARGE pruefen
- Mehrfachbeteiligung: darauf hinweisen, dass sich `{{buero.name}}` im selben Verfahren nicht zusaetzlich in anderer Konstellation (ARGE-Mitglied, Nachunternehmer eines Konkurrenten) beteiligen sollte, ohne die Ausschlussregeln der Bewerbungsbedingungen zu pruefen

### Referenzen
- Es zaehlen nur eigene Referenzen von `{{buero.name}}`
- Referenz-Matching (ANLEITUNG.md Schritt 4e) laeuft normal ueber die Buero-Referenzdatenbank
- ARGE-Referenzen aus der eigenen Historie zaehlen als vollwertige eigene Referenzen - keine Grenzfall-Markierung, keine Rueckfrage wegen Konstellation oder Leistungsanteil; ARGE-Rolle sichtbar lassen (ARGE-REGEL in ANLEITUNG.md Schritt 4e)

### Nachweise (ANLEITUNG.md Schritt 9)
- Alle Nachweise auf `{{buero.name}}` ausgestellt - Standard-Checkliste aus Schritt 9a, keine Zusatzdokumente
- Bietergemeinschaftserklaerung entfaellt; Verpflichtungserklaerungen Dritter nur, falls Nachunternehmer noetig werden (dann als eigene Aufgabe mit Vorlaufzeit listen)

---

## Hinweise fuer die HTML-Analyse

- Deckblatt: Bewerber-Zeile "Bewerber: `{{buero.name}}` (Einzelbewerbung)"
- In der Zusammenfassung die Konstellation nennen
