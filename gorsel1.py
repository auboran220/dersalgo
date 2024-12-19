import tkinter as libgorsel #
from tkinter import ttk as gorselNesne


def portaYazdir1():
    print("buton1 calisti")
    textBoxYazilanlar.set("buton1 calisti")

def portaYazdir2():
    print("buton2 calisti")
    textBoxYazilanlar.set("buton2 calisti")

pencere = libgorsel.Tk() 
pencere.title("Programin adi")
pencere.minsize(450,600)

textBoxYazilanlar = libgorsel.StringVar() 

checkbox1 = gorselNesne.Checkbutton(pencere)
checkbox1.place(x=100, y=100)

textbox1 = gorselNesne.Entry(pencere, textvariable=textBoxYazilanlar)
textbox1.place(x=100, y=250)

textbox2= gorselNesne.Entry(pencere, textvariable=textBoxYazilanlar)
textbox2.place(x=250, y=250)

buton1 = gorselNesne.Button(pencere,text="buton 1", command=portaYazdir1)
buton1.place(x=100, y=450)

buton2 = gorselNesne.Button(pencere,text="buton 2", command=portaYazdir2)
buton2.place(x=300, y=450)

pencere.mainloop()


 