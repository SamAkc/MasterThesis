# Notizen vom 27.07.2023

## Crowdsensing vs. Crowdsourcing

- Crowdsensing in der Literatur nicht einheitlich definiert, steht zusammen mit den Begriffen Participatory Sensing, Citizen Science und Civic Science für das Einbinden einer größeren Bevölkerungsgruppe bei der Lösung bestimtmer, meist wissenschaftlicher, Probleme (Richter 2013)
- Crowdsourcing bezeichnet die Auslagerung traditionell interner Teilaufgaben an eine Gruppe freiwilliger User

## Kurze Präsentation meiner Masterarbeit

- läuft seit Mai, voraussichtlich bis November diesen Jahres (und hoffentlich noch weiter)
- ich entwickle ein Tool, um den Bürgerverein Mitte und damit (in der Zukunft) Bamberg als Stadt zu unterstützen
- idealerweise wirds vom Verein eingesetzt
- Name "Bamberg messen 2.0"

## Motivation

- besonders in der letzten Zeit bemerkbar: sehr heiße Tage, statt z.T. unerträglich heiß
- wo sind die Unterschiede zu kühleren Gegenden in Bamberg? Warum?
- Führungspersonen erreichen
- Aspekt des Crowdsensings: Inwieweit kann euer Input die Entwicklung eines solchen Tools beeinflussen? Lohnt es sich, den Extraschritt zu gehen? Wenn ja, inwiefern und warum? Sollte dieser Aspekt in der Zukunft berücksichtigt werden?

## Konzept zeigen

s. Präsentation

## Anforderungen zeigen

- bereits Input von Prof. Foken und David bekommen
- was würdet ihr euch wünschen?
- eventuell Anforderungen zeigen, kurz darüber quatschen, aber Input sammeln
- Priorisieren

## Fragen

- Login-Methode (Nextcloud) einbinden
- realistisch, dass ihr mein Tool in zukünftigen Treffen des Vereins einsetzt?

## Notizen

- Start- und Endzeitpunkt für einen Kalendertag und diese Kurve ist sehr limitiert
- Vorhersage informationsarm, nur 5 als Favoriten hinzuzufügen, Heiko hätte gerne 11, letzte Woche vergleichen mit heute
- Annotationen kennen viele Leute nicht, Kommentare, jeder Sensor hat seinen eigenen Chat
- eine Gruppe von Messwerten zu einem Sensor führen einen Chat
- Wind- und Blitze etc.
Prof. Foken: 
Wenn wir auf der Heatmap bleiben, dann geht das nur, wenn ich eine gewisse Qualitätskontrolle vorschalte, sonst Nonsense, die lokalen Klimazonen zu hinterlegen, diese lokalen Klimazonen dann entsprechend der Daten dann diese Farbe zuzuordnen, Bild rastern, dann in das Raster rein, welche Klimazone was ist, dazu muss dahintergelegt werden, dass Qualitätskontrolle ist
-> Standardabweichung, Median etc.
Im Dialogverfahren analysieren "Warum haut der eine Sensor nicht hin?" -> neben dem Auslesen der Daten muss das Qualitätsmanagement kommen, ist die Temperatur in dem üblichen Temperaturbereichn ,den es geben kann, solche Grundsachen erstmal kontrolliert werden
Schützenstraße hat am Tag Waldklima, die wird da rausfliegen, weil das zu kalt ist -> später grundsätzlich drüber nachdenken, solche Effekte durch KI-Methoden zu erkennen und richtig zu interpretieren
- Schnittstellen schaffen, wo der nächste Ansetzen kann (Reem-Samet-Zukunft)
- für Toulouse, Amsterdam etc. schon gemacht, Bamberg ist kleiner, kleinräumliche Struktur, wie umzusetzen?

Eher Ausblick, wie mit den Daten verfahren werden soll
Foken: Problem, dass Bürgerverein als solcher interessiert ist, aber Uni nicht an Bürgerverein orientiert sondern an Smart City -> Leonie: korrekt
Heiko: Daten liegen kreuz und quer, haben sich Nextcloud gebucht, um Daten einheitlich zu verwalten, je nachdem was deren IT'ler

Einsetzen, wenns in einem mit arbeitbaren Zustand ist, auf jeden Fall, 
(Für mich abzuklären: Wie kann sowas langfristig gehosted werden? Welche Möglichkeiten gibt es?) -> NO

Was das BVM erreichen möchte: Wir wollen dass die Stadt Bamberg (wie die Stadt Wien) einen Hitzeplan der Stadt erstellt, wo sind die Punkte der Stadt, wos am wärmsten wird, wo sind kühlere Zonen etc., wo darf nicht gebaut werden,um diese Kaltluftströme nicht abzudecken -> nach dem Ermitteln dieser Hitze-Hotspots herausfinden, wie man das Bekämpfen kann
Hitzerelevante Punkte einbinden (Bäume, Brunnen, aus OSM z.B.) -> neue Anforderung?

Stadt Wien unbedingt auschecken, Cool-Spots, Brunnen, -> in Einleitung, Motivation, related Work mit vorstellen
Vorschlag an die Stadt geben, so kann das aussehen

Innenstadt bewohnbar halten, Hitzespots bekämpfen

Prozess im Verein durch so ein Tool zu unterstützen, automatisiert/durch EInsatz von simplen Tools, 
manuell

Zwei Zonen, Landing Zone, da landen alle Daten drin, werden nicht für Berechnung hergenommen, da steht dann "diese Daten sind noch nicht ausreichend verbessert"
Modul installiert, was die Daten automatisch verbessert, in Curated Zone verschiebt

Ich mach Möglichkeiten für Manuelle, 
Data Lake Architektur, wie so was heißt

Crowdcurating, Citizen-Science

Prof. Foken an Darstellungen:
BVM soll bisschen was suchen, was interessant ist
Zeiten aussuchen, in denen man was darstellen will, was ich immer mache ist, dass ich mir einen Monat angucke, und schaue was ist interessant
nicht bewölkt, sondern besondere Minima/Maxima, Struktur der Temp sehr divers im Stadtgebiet,
und dann in der Lage, in großen Zeitabschnitten angeguckt hat, kleine Zeitabschnitte (Tag, Mittagszeit) mehrere Stationen übereinander legt, eins macht dass man ein Mittel einer lokalen Klimazone bildet, und dann eine Station separat zeigt, und dann schaut, wie verhält sie sich separat
z.B . Klimazone Inennstadt, Innenhof Sternla, wann hat Sternla seinen Heizer eingeschaltet? 
Station hat Waldklima, etc. separat angucken

Bei uns in der Excel-Datei drinnen, Regressionsgeraden zwischen zwei Stationen können gezeigt werden
Warum haut die eine Station raus oder nicht? Was man später mit KI machen kann, wann ein Sensor von Sonne beschienen wird, lernt, und dann rausnimmt
Ihr habt doch die Excel-Dateien die ich mache, so ungefähr daran halten
In so einem Chat schaut er selten rein, Chat-Time festlegen, wo man dann gemeinsam reinguckt

Juni/Juli drüberscrollen, um Tropennächte ausfindig zu machen

Daniela: Oberfläche, Stationen ein-/ausschalten, wie eine Excel-Sicht, zeigt letzten Tag, alle Stationen angehakt, weghaken, will ich garnicht alle sehen, Anfangs-/Endzeitpunkt verschieben, dieser Zeitraum ist komisch, manuelles Zusammenbauen durch Auswählen/Anklicken etc., darüber will ich reden, "diese Ansicht merken", merkt sich alles (Stationen, Zeitraum etc.), codiert in URL-Link die Parameter z.B. (genau das was Prof. Foken mit Excel-Dateien macht)
Standard-Ansichten vordefinieren, Sommertage, Tropennächte, nicht jedes Mal von vorne anfangen -> Fokus auf Zeitreihen, Grafana als Web-Library für Zeitreihen-Analysen, Hacker-Backspace Bamberg
https://play.grafana.org/d/000000012/grafana-play-home?orgId=1&from=1690482764222&to=1690483080808

Hacker-Space auch selbst ein Tool entwickelt mit der Software im Kern "wie habt ihrs eingebunden, wie geht ihr damit um?"


in 1-2 Monaten noch einmal zusammensetzen
25. August in der Lagarde, 10-13 Uhr, Freitag
Fenner, CrowdQC+ 
