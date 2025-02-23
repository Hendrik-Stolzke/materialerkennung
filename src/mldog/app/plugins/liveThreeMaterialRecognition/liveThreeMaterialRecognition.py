import time
import tkinter
from typing import Literal
from mldog.app.model.core import Core
from mldog.app.plugins.liveMaterialRecognition.liveMaterialRecognition import ImgTrafficLight, TextField
from mldog.app.tasks.three_material_recognition_task import ThreeMaterialRecognitionTask
from mldog.app.ui.application import MLDOGApplication
import threading

from tkinter import TclError, ttk
import tkinter as tk


class LiveThreeMaterialRecognition(MLDOGApplication):
    def __init__(self,core: Core,parent: tkinter.Frame):
        MLDOGApplication.__init__(self,"LiveThreeMaterialRecognition",core,parent)
        


        label = ttk.Label(self._ui, text="Materialerkennung für zwei Materialien:", style='Heading.TLabel',font=("Arial",20))
        label.grid(column=0, row=0, pady=(20, 5),sticky="w")

        self.frame = tkinter.Frame(self._ui, highlightbackground="black", highlightthickness=4,width=800,height=500)

        self.frame.grid(column=0,row=1,columnspan=4)

        self.statusText = TextField(self.frame,"",("Arial",30))
        self.statusText.updateText("Bereit für Bohrung!")
        self.resultText = TextField(self.frame,"",("Arial",30))

        self.statusText.grid(column=1,row=1)
        self.resultText.grid(column=1,row=2)

        self.trafficLight = ImgTrafficLight(self.frame,parent.tk,padx=0,pady=0)

        self.trafficLight.grid(column=0,row=1,rowspan=2)
        self.trafficLight.green()

        
        self._core.setTask(ThreeMaterialRecognitionTask(),self.handleTaskResult)

        
    def handleTaskResult(self, message: tuple) -> None:

        if(message[0] == "start"):
            self.trafficLight.startBlink("green")
            self.statusText.updateText("Bohrvorgang...")
            self.resultText.clear()
        if(message[0] == "analysis"):
            self.trafficLight.startBlink("red")
            self.statusText.updateText("Analysiere...")
        if(message[0] == "result"):
            self.statusText.updateText("Bereit für Bohrung!")
            self.trafficLight.green()

            if(message[1] [0][0][0] == 1):
                self.resultText.updateText("Ergebnis("+str(int(message[1][1] * 1000) / 1000)+"s):\n-Holz!")
            elif(message[1] [0][0][1] == 1):
                self.resultText.updateText("Ergebnis("+str(int(message[1][1] * 1000) / 1000)+"s):\n-Kunststoff!")
            elif(message[1] [0][0][2] == 1):
                self.resultText.updateText("Ergebnis("+str(int(message[1][1] * 1000) / 1000)+"s):\n-Metall")
            else:
                self.resultText.updateText("Ergebnis("+str(int(message[1][1] * 1000) / 1000)+"s):\n-Holz: " + str((((message[1] [0][0][0]*100) * 1000) / 1000)) +"%\n-Kunststoff: " + str((((message[1] [0][0][1]*100 )* 1000) / 1000)) + "%\n-Metall: " + str((((message[1] [0][0][2]*100 )* 1000) / 1000)) + "%")    



TrafficLightColor = Literal["green","red"]
