# Entwicklung eines interaktiven Werkzeugs zur Kuratierung von Umweltdaten einer bürgerinitiierten Crowdsensing-Kampagne

<img src="/misc/mobi_logo.png" alt="MOBI-Logo" width="200" height="200">

In dieser Arbeit soll es darum gehen, den Bürgerinnen und Bürgern der Stadt Bamberg die Möglichkeit zu bieten, die Sensordaten des Klimamessnetzvereins Bamberg (BVM) einzusehen und durch die Funktion des Hinzufügens von Annotationen zu diesen, den Crowdsensing-Aspekt näher zu bringen. Dadurch ergeben sich die Leitfragen, inwieweit sich dies auf die Entwicklung eines solchen Tools auswirkt, inwiefern ein Ansatz wie dieser sinnvoll ist und in der Zukunft berücksichtigt werden sollte.

## Technische Umsetzung

![Architektur](doc/appendices/Architektur.png "Architektur")

- Python als Werkzeug zum Einbinden diverser, benötigter Frameworks
- Flask als Implementierung der Webapplikation (zunächst als Webserver)
- Jinja als Template-Engine für Flask
- PostgreSQL als Datenbank zum Speichern von Chats, Sensordaten, Credentials, Graphen und Feedback

## Schritte

1. docker-compose.yml
2. SQL-Query "tables.sql" ausführen
3. in Graphana einloggen und Daten nach Belieben manipulieren/visualisieren
4. ...

## Stakeholder

- Klimamessnetz Bamberg (BVM)
- Prof. Thomas Foken
- Projektgruppe des Lehrstuhls für Visualisierung von Fabian Beck (Mitglieder: Pascal Löffler und Florian Aschinger)
- MOBI-Lehrstuhl der Universität Bamberg

## Anforderungen

tba.
