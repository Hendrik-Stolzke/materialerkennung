from pathlib import Path
import tkinter
from typing import Literal
from PIL import Image, ImageTk

TrafficLightColor = Literal["green","red"]

class ImgTrafficLight(tkinter.Frame):
    def __init__(self,parent,tk,*args,**kwargs):
        tkinter.Frame.__init__(self, parent)
        self.tk = tk
        self.currentBlinkId = "init"
        
        self.greenImg = ImageTk.PhotoImage(Image.open(Path(__file__).with_name('green.png')))
        self.redImg = ImageTk.PhotoImage(Image.open(Path(__file__).with_name('red.png')))
        self.offImg = ImageTk.PhotoImage(Image.open(Path(__file__).with_name('off.png')))
        self.label = tkinter.Label(self,image=self.offImg,bg=None)
        self.label.pack(padx=0,pady=0)


    def off(self):
        if self.currentBlinkId != "init":
            self.stopBlink()

        self.label.configure(image=self.offImg)


    def green(self):
        if self.currentBlinkId != "init":
            self.stopBlink()

        self.label.configure(image=self.greenImg)

    def red(self):
        if self.currentBlinkId != "init":
            self.stopBlink()

        self.label.configure(image=self.redImg)

    def startBlink(self,color:TrafficLightColor):
        if self.currentBlinkId != "init":
            self.stopBlink()

        def blinkA():
            if(color == "green"):
                self.green()
            if(color == "red"):
                self.red()

            self.currentBlinkId = self.after(300,blinkB)


        def blinkB():
            self.off()

            self.currentBlinkId = self.after(300,blinkA)

        blinkA()

    def stopBlink(self):
        self.after_cancel(self.currentBlinkId)