# BambergEcoPulse
<img src="/misc/mobi_logo.png" alt="MOBI-Logo" width="100" height="100">

Diese Masterarbeit stellt die Planung und Implementierung einer Anwendung zur Kuratierung von Umweltdaten einer bürgerinitiierten Crowd\-sen\-sing-Kampagne vor. Motiviert durch den Klimawandel zielt die Arbeit darauf ab, sowohl eine Softwarelösung zum Fördern von Maßnahmen zur Verlangsamung des Klimawandels zu entwickeln, als auch die Bürger*innen in Bamberg zu motivieren, sich an einer Crowdsensing-Kampagne zu beteiligen. Das vorgestellte Konzept erläutert die Vorgehensweise in der Arbeit, um darauf basierend die Anforderungen zu erheben und zu analysieren. Auf Grundlage der Anforderungen wird die Softwarearchitektur entworfen und die Implementierung der Anwendung beschrieben. 

Die Ergebnisse der Arbeit fallen dabei positiv aus. Die entwickelte Anwendung erfüllt einen überwiegenden Teil der Anforderungen und kann als Grundlage für weitere oder zukünftige Arbeiten dienen. Die Zusammenarbeit mit den Stakeholdern hat sich als hilfreich erwiesen, um die Anforderungen zu erheben. Zusätzlich hat sich der iterative Ansatz der agilen Softwareentwicklung als ideale Vorgehensweise für die Entwicklung der Anwendung herausgestellt, da eine schnelle und auf die Stakeholder zugeschnittene Entwicklung möglich gewesen ist. Die aufgestellten Anforderungen stimmen mit der Literatur überein, weswegen der Crowdsensing-Ansatz in der Softwareentwicklung zwar sinnvoll ist, aber auch mit Herausforderungen, welche mit einem Mehraufwand verbunden sind, einhergeht.

Damit reiht sich die Arbeit in die Forschungslücke der Entwicklung von Crowdsensing-Anwendungen ein und kann als Grundlage für weitere Arbeiten dienen, um die Anwendung zu erweitern oder zu verbessern.

## Architecture

![Architektur](doc/appendices/Architektur.png "Architektur")

## Prerequisites

You will need Docker installed on your machine, check [here](https://www.docker.com/get-started/).

## Setup

First run...
```
cd /app
```

...then...
```
docker compose up
```
...enjoy!

## Stakeholder

- [Bürgerverein Bamberg Mitte e.V. (BVM)](https://bvm-bamberg.de/de/home/)
- [Domänenexpert*innen (Mikrometeorologe der Universität Bayreuth)](https://www.micrometeorology.de/)
- [Lehrstuhl für Informatik, insbesondere Mobile Softwaresysteme/Mobilität der Otto-Friedrich-Universität Bamberg](https://www.uni-bamberg.de/mobi/)

## Problem Area

- connect Grafana iframe to Flask application
- make application deployable on all machines without needing to setup data every single time
- get station data automatically
- import KML files to OpenStreetMap

## Solution Area

- run flask instance on Docker as well
- run init.sql to set up database when composing 
- let Grafana point to provision directories so dashboards are set up when composing