from tkinter import *

def bigger(self):
    self["font"]=("Hel")

def smaller(self):
window=Tk()

label=Label(window, text="Hello, World!", font=("Helvetica", 16))
label.pack()

b1=Button(window, text="폰트를 크게", command=bigger(label))
b1.pack()

b2=Button(window, text="폰트를 작게", command=smaller(label))
b1.pack()
