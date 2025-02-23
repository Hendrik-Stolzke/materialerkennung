from pathlib import Path
import tkinter
from tkinter.tix import IMAGETEXT
from typing import Literal
from mldog.app.model.core import Core
from mldog.app.plugins.liveMaterialRecognition.materialDetection.util.trafficLight.imgTrafficLight import ImgTrafficLight
from mldog.app.plugins.plot.drill_plot_app import DrillProcedurePlotUI, PlotUI
from mldog.app.plugins.plot.drill_plot_model import ApplicationState, DrillPlotModel
from mldog.app.tasks.material_recognition_task import MaterialRecognitionTask
from mldog.app.ui.application import MLDOGApplication

from tkinter import Image, ttk


class LiveMaterialRecognition(MLDOGApplication):
    def __init__(self,core: Core,parent: tkinter.Frame):
        MLDOGApplication.__init__(self,"LiveMaterialRecognition",core,parent)
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

        
        
        self._core.setTask(MaterialRecognitionTask(),self.handleTaskResult)


        
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
            else:
                self.resultText.updateText("Ergebnis("+str((int(message[1][1] * 100) *1000) / 1000)+"s):\n-Holz: " + str((int(message[1] [0][0][0]*100) * 1000) / 1000) +"%\n-Kunststoff: " + str((int(message[1] [0][0][1]*100) * 1000) / 1000) + "%")    

TrafficLightColor = Literal["green","red"]
class TextField(tkinter.Frame):
    def __init__(self,parent: tkinter.Frame ,initMessage:str,font:tuple):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.font = font

        self.label = ttk.Label(self,font=font)
        if(initMessage != ""):
            self.updateText(initMessage)
        self.label.pack()

    def updateText(self,newMessage:str):
        self.label.config(text=newMessage,relief="raised")  

    def clear(self):    
        self.label.config(text="",relief="flat")   

class TrafficLight(tkinter.Widget):
    def __init__(self,parent:tkinter.Frame,scale:int,tk:tkinter.Tk,gridRow,gridColumn):
        self.parent = parent
        self.scale = scale
        self.tk = tk
        self.currentBlinkId = "init"
        self.gridRow = gridRow
        self.gridColumn = gridColumn

        self.canvas = tkinter.Canvas(parent,width=scale,height=scale*4)
        self.canvas.create_rectangle(0,0,scale,scale*2,fill = "gray")
        self.canvas.create_rectangle(3*scale/7,scale*2,4*scale/7,scale*4,fill="black")

        self.greenLight = self.canvas.create_oval(0,0,scale,scale,fill="LightGray")
        self.redLight = self.canvas.create_oval(0,scale,scale,scale*2,fill="LightGray")

        self.canvas.grid(rowspan=4,column=self.gridRow,row=self.gridColumn,sticky="w")

    def off(self):
        if self.currentBlinkId != "init":
            self.stopBlink()

        self.greenLight = self.canvas.create_oval(0,0,self.scale,self.scale,fill="DarkRed")
        self.redLight = self.canvas.create_oval(0,self.scale,self.scale,self.scale*2,fill="Green")

        self.canvas.grid(column=self.gridRow,row=self.gridColumn)

    def green(self):
        if self.currentBlinkId != "init":
            self.stopBlink()

        self.greenLight = self.canvas.create_oval(0,0,self.scale,self.scale,fill="DarkRed")
        self.redLight = self.canvas.create_oval(0,self.scale,self.scale,self.scale*2,fill="LimeGreen")

        self.canvas.grid(column=self.gridRow,row=self.gridColumn)

    def red(self):
        if self.currentBlinkId != "init":
            self.stopBlink()

        self.greenLight = self.canvas.create_oval(0,0,self.scale,self.scale,fill="OrangeRed")
        self.redLight = self.canvas.create_oval(0,self.scale,self.scale,self.scale*2,fill="Green")

        self.canvas.grid(column=self.gridRow,row=self.gridColumn)

    def startBlink(self,color:TrafficLightColor):
        if self.currentBlinkId != "init":
            self.stopBlink()

        if color == "green":
            self.color1A = "DarkRed"
            self.color2A = "Green"
            self.color1B = "DarkRed"
            self.color2B = "LimeGreen"
        elif color == "red":
            self.color1A = "OrangeRed"
            self.color2A = "Green"
            self.color1B = "DarkRed"
            self.color2B = "Green"

        def blinkA():
 
            self.greenLight = self.canvas.create_oval(0,0,self.scale,self.scale,fill=self.color1A)
            self.redLight = self.canvas.create_oval(0,self.scale,self.scale,self.scale*2,fill=self.color2A)
            
            self.canvas.grid(column=self.gridRow,row=self.gridColumn,sticky="w")

            self.currentBlinkId = self.after(300,blinkB)


        def blinkB():
            self.greenLight = self.canvas.create_oval(0,0,self.scale,self.scale,fill=self.color1B)
            self.redLight = self.canvas.create_oval(0,self.scale,self.scale,self.scale*2,fill=self.color2B)
            
            self.canvas.grid(column=self.gridRow,row=self.gridColumn,sticky="w")

            self.currentBlinkId = self.after(300,blinkA)

        blinkA()

    def stopBlink(self):
        self.after_cancel(self.currentBlinkId)