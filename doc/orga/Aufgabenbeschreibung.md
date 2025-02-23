# Akkubohrer - Materialerkennung Schichtplatten

<div align="center">
    <img src="img/bohren.jpg" width="50%">
    <img src="img/schichtplatte.png" width="18.92%">
</div>

## Um was geht es?

Mit unserem Bohrer sind wir in der Lage Strom, Spannung und Sound während des Bohrvorgangs zu messen.
Ist es möglich, allein anhand dieser Daten Aussagen zu machen, in welches Material gerade gebohrt wurde?
Und lassen sich so auch die verborgenen Materialien einer Schichtplatte rekonstruieren?

## Ziel

Zentrales Ziel dieses Projekts ist die Entwicklung eines Live-Systems, das nach einem Bohrvorgang sagen kann, in welche Materialschichten gebohrt wurde.

Bei erfolgreicher Umsetzung kann das System Teil eines Demonstrators werden, der bei Studieninformationstagen oder Messen eingesetzt wird.

## Welche Teilschritte sind erforderlich?

1. Konzeption und Durchführung von Datenaufzeichnungen
2. Feature-Extrahierung aus Zeitreihendaten
3. Training und systematische Evaluation verschiedener ML-Modelle (Klassifikatoren)
4. Integration in existierenden Demonstrator (GUI-Anwendung), um on-the-fly neue Daten aufnehmen und vorhersagen machen zu können und das Ergebnis einem Nutzer zu präsentieren
5. Weitere mögliche Aufgaben:
   - Geschwindigkeitsoptimierung (z.B. Subsampling der Signale) und Untersuchung deren Einfluss auf die Vorhersagegenauigkeit
   - Untersuchung des Einflusses der Split-Größe auf die Vorhersagegenauigkeit
   - Untersuchung / Vergleich von mehr als 2 Materialien / Materialschichten
   - Umsetzung geeigneter Visualisierungen zur besseren Veranschaulichung für den Benutzer
