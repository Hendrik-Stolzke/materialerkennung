# Projektplan

## Gemeinsame Vision:
Vom Benutzer wird entweder in Holz, Kunststoff oder Metall gebohrt, das System soll nach dem Bohrprozess erkennen, in welches Material gebohrt wurde. Der Benutzer nimmt den Bohrer und startet das Programm. Er wählt das zu bohrende Material aus und bereitet den Bohrprozess vor. Nach dem Start des Programms und dem Anschließen des Bohrers erhält der Benutzer ein "Bereit"-Signal, zum Beispiel ein Audiosignal „Bohrung startbereit“ und ein grünes Licht auf dem Bildschirm. Er kann nun mit dem Bohren beginnen. Während des Bohrvorgangs erhält der Benutzer auf dem Bildschirm ein "Aufnahme"-Signal, und am Ende des Bohrens wird ihm mitgeteilt, in welches Material er gebohrt hat (zum Beispiel ein Icon des Materials und ein Text, welcher zeigt, wie sicher das System das Ergebnis einschätzt). Dem Benutzer werden auch die aufgezeichneten Signale in einem Diagramm angezeigt. 

### Angehende Ziele des Teams
1. Materialerkennung zwischen zwei Stoffen (Holz-Spannplatte/Kunststoff-PC)
2. Materialerkennung zwischen drei Stoffen (Holz-Spannplatte/Kunststoff-PC/Metall-xxx)
3. Erkennung des Materials in Schichtplatten
4. Live-Materialerkennung
5. Unterscheidung der einzelnen Materialien in Unterarten (z. B. Holz: Eiche, Mahagoni, Ahorn, etc.)

### Aktionen des Nutzers:
1. Um die Materialerkennung zu starten muss das Programm auf dem Rechner des Users gestartet und der Bohrer angeschlossen werden
2. Für das Starten der Bohrung muss der Bohrer manuell angeschlossen und vorbereitet werden.
3. Der User startet die Messung und bohrt durch die gewählten Materialien. 
4. Nach Vollendung der Bohrung erhält der User anhand der Messung ein Ergebnis. Daraus geht der/die Stoff/e hervor, der/die durchbohrt wurde/n.
5. Für eine weitere Bohrung wiederholt der User zusätzlich den Schritt 2 oder nur Schritt 3,4 und 5.
### Erwartungen des Nutzers:
1. Ein Signal zum Beginn erhalten
2. Für eine reibungslose und effiziente Anwendung werden während der Programmnutzung regelmäßige Statusupdates (wie z. B. 'Bohrer erkannt', 'Input wird analysiert' etc.) eingeblendet
3. Darstellung des Ergebnisses: die Vorhersage des Materials wird mithilfe einer benutzerfreundlichen  GUI dem User präsentiert 
## Softwarekomponenten:
    - GUI 
        -Fenster öffnet sich bei Programmstart.
        -User kriegt eindeutige Statusanzeigen(visuell):
            -"Bereit für Bohrung!"
            -"Bohrvorgang erkannt!"
            -"Analysiere!"
        -User sieht Ergebnis der Analyse (evtl. mit unterstützenden Icons):
            -"[Material_1] : [x]%"
            -"[Material_2] : [y]%"
        -User hat Auswahl zwischen [neue Bohrung?] oder [Details anzeigen?].
    - Messungs- und Datenverwaltung
        - Dateisystem zum Speichern und organisieren von Rohdaten
        - Datenbereinigung
        - Feature Engineering
        - Datenvisualisierungstools
    - ML-Pipeline
        - Modelltraining & Entwicklung
        - Modell Überwachung und Optimierung
            - Hyperparameter Einstellungen und Optimierung
## Hardwarekomponenten:
    - Akkubohrer
    - Bohrer (vorerst M6)
    - Akkumulatoren
    - Schraubzwinge
    - Messbox
    - Kabel ???
    - Laptop
    - Materialien (vorerst Holz-Spannplatte/Kunststoff-PC)
## ML-Aufgabe:
    - Ziel: Präzise Bestimmung der gebohrten Materialien anhand von Sensorwerten
    - Lernart: Supervised Learning (überwachtes Lernen)
    - Art: Klassifikation
    - Algorithmen: Decision Tree, Random Forest, KNN, SVM, u.w.
    - Daten: Gelabelte Messwerte von Sensoren, einschließlich Ton, Stromverbrauch und Spannung als Zeitreihendaten, sowie die Zielvariable (Material)
    - Datenverarbeitung: Bereinigung der Daten,Erstellen der IDs, Rauschentfernung und Vorbereitung der Daten für die Verwendung in den ML-Algorithmen.
    - Training und Testen: Aufteilung der Daten in Trainings- und Testdaten, typischerweise 70-80% für das Training und 20-30% für Tests.
    - Optimierung: Tuning der Hyperparameter mittels Gridsearch und Fachwissen sowie durch Testen verschiedener Konfigurationen.
    - Auswertung: Bewertung der Genauigkeit des Modells, Identifizierung von Fehlern und Ableitung von Verbesserungsmöglichkeiten.
    - Bereitstellung: Implementierung des Modells, entweder integriert in einer Anwendung oder als API zur Ergebnisübermittlung.
    - Monitoring: Überwachung der Modellgenauigkeit über die Zeit, Anpassung des ML-Algorithmus bei Bedarf 
      (z. B. bei neuen Durchbrüchen oder sich ändernden Anforderungen) und Durchführung von Ergebnisanalysen.
## Teilschritte:
### Phase 1:
1. Projektplanung
2. Auseinandersetzen und Visualisieren der (alten) Daten
3. Einarbeitung in Git
4. Erste Datenerhebung
5. Feature Engineering (1) 
    * Einlesen der Dateien
    * Zusammensetzen der Dateien
    * Hinzufügen der IDs
    * Konvertierung zu Dataframe
    * Feature Extrahierung mit MinimalFCParameters
    * Feature Selektion (30 -> 10 mit select_features)
    * extra Selektion der eigenen Merkmale aus der vorherigen Liste an Features (10 -> 5)
    * Anhängen des Zielmerkmalvektors
    * Umwandlung in csv-Datei
6. ML-Pipeline zur Erreichung der Baseline (MVP) (1) inkl. der Wahl des passenden Algorithmen bzgl. der vorhandenen Daten und Features
7. Umwandlung der Methoden des Feature Engineerings in MLDOG Framework (zur Übung)
8. Vorstellung der BETA GUI anhand einer Skizze und des Prototyps (siehe Softwarekomponenten: GUI)
### Phase 2:
1. Feature Engineering (2) 
    * Recherche bzgl. der Extraktionsmethoden und derer Parameter
    * Extrahierung der Merkmale mit Hilfe der gewählten Methode und der optimalen Parameter in einzelne Dateien
    * Visualisierung der Features und Überprüfung auf Korrelation mithilfe der Korrelationsmatrix und Entfernen der korrelierender Merkmale
    * Selektion der Merkmale mit entweder 1. Forward Selection und 2. Backward Elimination oder Embedded Methods
2. Findung und Entscheidung über die besten Features und des Algorithmus anhand einer Tabelle mit Ranking der Accuracy aus der Klassifikation mit verschiedenen Algorithmen (DesicionTree, RandomForest, knn, NaiveBayes und SoftVoting(DesicionTree, knn, NaiveBayes)) mit default Parametern
3. Hyperparameteroptimierung mit dem gewählten Modell aus Schritt 2. mit CrossValidation/GridSearch
4. Testen des Modells mit den gewählten Parametern und Darstellung in der Konfusionsmatrix
5. Aktualisieren des MLDOG Frameworks mit den neuen Methoden und Pipeline und Fertigstellen der GUI
6. Testdatenerhebung (2. Bohrung: Holz/Kunststoff mit jeweils 12 erfolgreichen Bohrungen) zum Testen (mit 1/3 der neuen Daten) des bis dahin fertigen Modells 
### Phase 3:
1. 3. Bohrung (Metall)
2. Hinzufügen von 32 Aufnahmen zu den vorhandenen Bohrungen (Holz/Kunststoff)
3. Anwenden der Vorverarbeitungsschritte auf dem gesamten Datensatz (Holz/Kunststoff/Metall)
4. Bestimmung der neuen Hyperparameter mit dem gewählten Modell aus Phase 2, Schritt 2.
5. Training der ML-Pipeline mit den gewählten Parametern
6. Evaluierung mithilfe der Konfusionsmatrix
7. Testdatenerhebung (4. Bohrung: Holz/Kunststoff/Metall mit jeweils 8 erfolgreichen Bohrungen) zum Testen des Modells 

## Minimum Viable Product:
Bestimmung eines Materials durch Klassifikation aus zwei zuvor trainierten verschiedenen Stoffen
(Holz-Spannplatte/Kunststoff-PC) mit einer 
Klassifikationsgenauigkeit von mehr als 50% (Baseline).
