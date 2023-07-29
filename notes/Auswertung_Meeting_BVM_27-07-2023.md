# Auswertung des Meetings vom 27.07.2023

## Zusätzliche Anforderungen

- Annotationen lieber Chat nennen (verständlicher für Nutzer)
- nicht die Informationskurve von Netatmo verwenden, da diese sehr limitiert ist. Lieber: Start-/Endzeitpunkt für einen Kalendertag definieren
- Möglichkeit, mehr Favoriten hinzufügen zu können (Heiko hat die Zahl 11 in den Raum geworfen, warum nicht unbegrenzt?)
- Umsetzung eines Chats soll im Gesamten zu einem Sensor passieren, nicht für einzelne Sensordatenauslesungen
- Qualitätskontrolle muss vor Heatmap geschalten werden, da der Sinn und Zweck der Heatmap durch Fehler/Ausreißer verloren geht (mit Standardabweichung, Median etc. arbeiten. Für mich bedeutet das: Einer zukünftigen Masterarbeit überlassen oder qualitätskontrollierte Daten heranziehen, eventuell sogar KI-Methoden einsetzen, das aber eindeutig dann zukünftige Masterarbeit/Projektarbeit)
- Wunsch, Daten einheitlich zu organisieren, da derzeitiger Stand verschiedene Plattformen sind. Nextcloud bereits im Einsatz, aber muss eingepflegt werden
- Hitzerelevante Landmarks sollen in die Karte eingebunden werden (Bäume, Wälder, Brunnen etc., anscheinend mit OSM möglich)
- grundlegend wünscht sich der Verein/Prof. Foken, dass diverse Analysen mithilfe meines Tools möglich sein sollen. Konkret bedeutet das, Minima/Maxima einer Mittagszeit/eines Tages/einer Woche/eines Monats auslesen und vergleichen zu können, Temperaturunterschiede in den verschiedenen Strukturen der Innenstadt sinnvoll aufzeigen zu können und verschiedene Mittel verschiedener Wetterstationen miteinander vergleichen zu können (grob gesagt: "Nachricht an den Mann bringen mithilfe diverser Analysen durch die Verwendung meines Tools")
- Visualisierung: alle Stationen anzeigen/ausblenden, einzelne Stationen anzeigen/ausblenden, Anfangs-/Endzeitpunkt verschieben, manuelles Zusammenbauen von Sensoren und Zeiten, Schaltfläche zum Ansicht merken (als Favorit hinzufügen z.B.), Standard-Ansichten vordefinieren (Sommertage, Tropennächte...)

## Misc

- Zeitreihen-Analysen durch Web-Library [Grafana](https://play.grafana.org/d/000000012/grafana-play-home?orgId=1&from=1690482764222&to=1690483080808)
- Hacker-Space hat ebenfalls eine Software mit so einer Funktion im Kern entwickelt, die fragen wie so etwas eingebunden und damit umgegangen wird
- Begrifflichkeiten abklären: Crowdsensing vs. Crowdsourcing vs. Crowdcurating vs. Citizen-Science
- Daten sollen in zwei Pools untergliedert werden: Landing Zone, in welcher alle Daten unkuratiert darin landen, werden für Berechnung nicht herangezogen, mit Hinweis "diese Daten sind noch nicht ausreichend verbessert" & Curated Zone, mithilfe eines installierten Moduls, welche Daten automatisch verbessert, werden für Berechnungen herangezogen -> Data Lake Architektur
- Ziel des BVM: Bamberger Innenstadt bewohnbar halten, Hitzespots bekämpfen
- Stadt Wien als ideale Related Work Quelle (s. Heikos E-Mail)
- Frage des Hostings abklären: BVM vs. Uni vs. andere Möglichkeit (AWS-Hosten meinerseits?)
- nächstes Treffen am 25.08.2023 in der Lagarde 1 von 10-13 Uhr
