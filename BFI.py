from PySide6.QtCharts import QBarSeries, QBarSet, QChart, QBarCategoryAxis, QValueAxis
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow, QApplication
from ui_main import Ui_frm_main
import csv


class Frm_main(QMainWindow, Ui_frm_main):
    def __init__(self):                             #### Initialisierung und Button Definition
        super().__init__()
        self.setupUi(self)
        
        #### übergreifende Variablen setzen
        self.inventory = []
        self.inventoryCount = 0
        self.result = []
        self.progVal = 0

        ## STARTSEITE
        ##########################################################################################################
        self.btn_start.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_inv))
        self.btn_start.clicked.connect(self.startQuest)

        ## BEFRAGUNG
        ##########################################################################################################
        self.btn_next.clicked.connect(self.nextQuestion)
        self.btn_finish.clicked.connect(self.lastQuestion)

        ## ERGEBNIS
        ##########################################################################################################
        self.btn_main.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_start))
    
    def startQuest(self):                           #### Startet die Befragung und setzt die ersten Werte
        #### Button ein-/ausblenden
        self.btn_finish.hide()                  # Button für letzte Frage ausblenden
        self.btn_next.show()                    # Next Button einblenden

        #### Variablen einleiten
        self.inventory = []                     # Inventory leeren
        self.inventoryCount = 0                 # Zähler für Fragen zurücksetzen
        self.progVal = 0                        # Progressbar zurücksetzen
        self.prog_bar.setValue(self.progVal)   
        self.openInventory()                    # Inventory befüllen
        self.setQuestion()                      # Erste Frage bereitstellen

    def nextQuestion(self):                         #### stellt die nächste Frage bereit und kodiert die gegebene Antwort
        #### Prüfen ob eine Antwort gegeben wurde
        if self.Abfrage() == False:
            return

        #### kodierung der gegebenen Antwort, Ablage und Auswahl aufheben        
        self.Coding()
        self.unSelect()

        #### nächste Frage vorbereiten und bereitstellen
        self.inventoryCount += 1                # Zähler hochzählen
        if self.inventoryCount >= len(self.inventory)-1:    # prüft ob die letzte Frage erreicht wurde
            self.btn_next.hide()                # wenn ja, wird der next button ausgeblendet
            self.btn_finish.show()              # und der letzte Frage button eingeblendet
        self.setQuestion()                      # stellt neue Frage bereit
        self.updateProgres()                    # updated den Fortschrittsbalken

    def lastQuestion(self):                         #### wird bei beantwortung der letzten Frage genutzt. Ruf Ergebnisseite auf und startet Auswertung
        #### Prüfen ob eine Antwort gegeben wurde
        if self.Abfrage() == False:
            return

        #### kodierung der gegebenen Antwort, Ablage und Auswahl aufheben 
        self.Coding()
        self.unSelect()

        #### Ruf die letzte Seite mit den Ergebnisgrafiken auf
        self.stackedWidget.setCurrentWidget(self.pg_end)

        supKat, supKatVal, subKat, subKatVal = self.calculation()   # Kalkulation der Ergebnisse
        self.updateCharts(supKat,supKatVal,self.grph_bar1, 60)      # Erstellung der Chart der Domänen
        self.updateCharts(subKat, subKatVal,self.grph_bar2, 20)     # Erstellung der Chart der Facetten

    def Coding(self):                               #### (re)kodiert die Antworten auf basis den Inventory
        if self.slct_a1.isChecked():
            val = 1
        elif self.slct_a2.isChecked():
            val = 2
        elif self.slct_a3.isChecked():
            val = 3
        elif self.slct_a4.isChecked():
            val = 4
        elif self.slct_a5.isChecked():
            val = 5
        
        self.inventory[self.inventoryCount][4] = val                #Rohwert
        # positive kodierung = 1 bis 5
        # negative kodierung => rekodierung = 6 - (1 bis 5)
        if self.inventory[self.inventoryCount][1] == "-":           # rekodiert bei negativer Polung
            self.inventory[self.inventoryCount][5] = 6-val
        else:
            self.inventory[self.inventoryCount][5] = val

    def setQuestion(self):                          #### wählt nächste Frage aus Inventory aus
        self.lb_question.setText(self.inventory[self.inventoryCount][0])

    def calculation(self):                          #### Berechnet die Wert-Serien  für die Charts

        sums_dict = {}
        for row in self.inventory:
            key = row[2]  # Wert aus Spalte 2
            value = int(row[5])  # Wert aus Spalte 5, angenommen es sind Zahlen
            if key in sums_dict:
                sums_dict[key] += value
            else:
                sums_dict[key] = value

        supKat = []
        supKatVal = []
        for key, value in sums_dict.items():
            supKat.append([key])
            supKatVal.append([value])

        sums_dict = {}
        for row in self.inventory:
            key = row[3]  # Wert aus Spalte 2
            value = int(row[5])  # Wert aus Spalte 5, angenommen es sind Zahlen
            if key in sums_dict:
                sums_dict[key] += value
            else:
                sums_dict[key] = value

        subKat = []
        subKatVal = []
        for key, value in sums_dict.items():
            subKat.append([key])
            subKatVal.append([value])

        return supKat, supKatVal, subKat, subKatVal

    def updateCharts(self, kat, val, graph, max):   #### Erzeugt einen Chart für die Auswertung. Wird zwei mal abgerufen
         
        series = QBarSeries()

        bar_set_Kat = QBarSet("")
        for value in val:
            bar_set_Kat.append(value)

        series.append(bar_set_Kat)

        chart = QChart()
        chart.addSeries(series)
        
        axis_x = QBarCategoryAxis()
        for value in kat:
            axis_x.append(value)
        if len(kat) > 6:
            axis_x.setLabelsAngle(90)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setRange(0,max)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        chart.legend().setVisible(False)

        graph.setChart(chart)

    def updateProgres(self):                        #### Updated den Fortschrittsbalken bei Fragenbeantwortung
        self.progVal += (100/60)
        self.prog_bar.setValue(self.progVal)

    def unSelect(self):                             #### Hebt die Antwortauswahl vor anzeigen der nächsten Frage auf
        self.slct_a1.setAutoExclusive(False)
        self.slct_a2.setAutoExclusive(False)
        self.slct_a3.setAutoExclusive(False)
        self.slct_a4.setAutoExclusive(False)
        self.slct_a5.setAutoExclusive(False)

        self.slct_a1.setChecked(False)
        self.slct_a2.setChecked(False)
        self.slct_a3.setChecked(False)
        self.slct_a4.setChecked(False)
        self.slct_a5.setChecked(False)  

        self.slct_a1.setAutoExclusive(True)
        self.slct_a2.setAutoExclusive(True)
        self.slct_a3.setAutoExclusive(True)
        self.slct_a4.setAutoExclusive(True)
        self.slct_a5.setAutoExclusive(True)         

    def Abfrage(self):                              #### Prüft, ob eine der Antwortmöglichkeiten ausgewählt ist.
        if self.slct_a1.isChecked() == False and self.slct_a2.isChecked() == False and self.slct_a3.isChecked() == False and self.slct_a4.isChecked() == False and self.slct_a5.isChecked() == False:
            return False
       
    def openInventory(self):                        ### Ruft das Inventory aus der .csv Datei auf   
        with open('BFI2.csv', newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=';')
            rowCount = 0
            for row in csv_reader:
                if rowCount >= 60:
                    break
                self.inventory.append(row[:6])
                rowCount += 1
 
app = QApplication()
frm_main = Frm_main()
frm_main.show()
app.exec()