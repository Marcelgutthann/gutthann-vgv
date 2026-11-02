---
name: vgv-verfahren
description: Nimmt die Unterlagen eines VgV-Verfahrens (von competitionline oder einem Vergabeportal geholt) in der Sitzung an, legt den Verfahrensordner unter N:\13. VGV\2-Laufende VgV an, legt die Karte im VgV-Radar des GHIW-Boards an und analysiert das Verfahren – nach dem verbindlichen Ablauf aus dem GHIW-Board. Ebenso für Nachträge zu laufenden Verfahren (Bieterantworten, Änderungen, Einladung Phase 2, Absage, Zuschlag). Triggert IMMER bei "/vgv", "neues VgV-Verfahren", "hier sind die Unterlagen", "von competitionline", "Ausschreibung anlegen", "VgV-Karte anlegen", "VgV-Analyse", "Nachtrag zum Verfahren", "Bieterantworten sind da", "neue Unterlagen zur VgV", "Einladung zum Verhandlungsgespräch". NICHT für die Präsentation selbst (Skill vgv-praesentation) und nicht für Referenzblätter (Skill referenzblatt).
---

# VgV-Verfahren aus der Sitzung

Auftakt, Ablauf, Nachtrag, Analyse-Anleitung, Bewerber- und Rollenprofile und Bürodaten liegen **im GHIW-Board** – nicht in diesem Plugin. Dieses Plugin ist nur der Zeiger.

1. Board-Werkzeug `vorlage` mit `schluessel: vgv` aufrufen. Große Teile kommen als Download-Link: mit `curl -o <dateiname> "<url>"` unverändert speichern, nie abschreiben.
2. **Neues Verfahren:** zuerst `teil auftakt` vollständig abarbeiten (Unterlagen lesen, Dublette prüfen, Verfahren und Konstellation bestätigen lassen, Auftragsblatt). Ohne bestätigtes Auftragsblatt kein Ordner und keine Karte. Danach `teil ablauf` Schritt für Schritt.
3. **Neue Unterlagen zu einem laufenden Verfahren:** `teil nachtrag`.
4. Werkzeuge im Board: `vgv_karte_anlegen`, `vgv_karte_setzen`, `vgv_dashboard`, `board`, `todo_detail`, `todo_zuweisen`, `kommentar_anlegen`, `unterpunkt_anlegen`, `unterpunkt_setzen`.

Ohne Board-Verbindung: nicht anlegen. Sag der Person, dass das GHIW-Board in Claude verbunden sein muss, und hör dort auf.
