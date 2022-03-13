from tkinter import *
import tkinter as tk
from tkinter import messagebox
import numpy as np
import random, sys, string
from PIL import ImageTk,Image
frame = tk.Tk()
# okno.bgcolor('lightblue')
# okno.setup(width=400, height=500, startx=200, starty=200)
frame.title('Projekt')
#topFrame = Frame(frame)
#topFrame.pack()
bottomFrame = Frame(frame)
bottomFrame.pack(side=BOTTOM)
#frame.geometry("400x300+200+200")
frame.geometry("900x1000+900+10")
my_scroll = Scrollbar(frame)
my_scroll.pack(side=RIGHT,fill=Y)

okno = Frame(frame)
okno.pack()

#Slownik---------------------------------------------------------------------------------------------------#

titleslownik = Label(text="SŁOWNIK",bg='black',foreground='white')
titleslownik.pack()
slownik={'dane osobowe':{'imie':'Jan','nazwisko':'Kowalski'},'zawod':['programista','analityk'],'wiek':[32]}

def wyswietlanieSlownika():
    t=str(asd.get())
    labelSlownik.config(text="Twoj slownik to " + str(slownik))
    labelKluczeSlownika.config(text="Klucze w slowniku to: " + str(list(slownik.keys())))
buttonWysSlownik=Button(text="Twoj slownik",command=wyswietlanieSlownika)
buttonWysSlownik.pack()   
labelSlownik=Label()
labelSlownik.pack()

def iloscKluczy():
    t=str(asd.get())
    messagebox.showinfo("Ilosc kluczy","Ilosc kluczy to: " + str(len(slownik)))
labelKluczeSlownika=Label()
labelKluczeSlownika.pack()
buttonIloscKluczy=Button(text="Ilosc kluczy",command=iloscKluczy)
buttonIloscKluczy.pack()

    
def wyswietlaniePozzKluczy():
    t=str(asd.get())
    #l15.config(text="Element/y w pozycji " + str(t) + " to " + str(slownik[t]))
    messagebox.showinfo("Element/y","Element/y w pozycji " + str(t) + " to " + str(slownik[t]))
asd = Entry()
asd.pack()
buttonWyswXKlucza=Button(text="Wyswietl dane z klucza",command=wyswietlaniePozzKluczy)
buttonWyswXKlucza.pack()


def dodawanieElementu():
    g=str(entryDodawanyElement.get())
    g1=str(dodajElement.get())
    slownik[g].append(g1)
    #labelDodanyELement.config(text="Dodales " + str(g1) + " do klucza: " + str(g))
    messagebox.showinfo("Dodales","Dodales " + str(g1) + " do klucza: " + str(g))
    labelSlownik.config(text="Twoj slownik to " + str(slownik))
    labelKluczeSlownika.config(text="Klucze w slowniku to: " + str(list(slownik.keys())))
labelDodanyELement = Label()
labelDodanyELement.pack()
labelDodawania=Label(text="Wpisz co chcesz dodac")
labelDodawania.pack()
dodajElement=Entry()
dodajElement.pack()

labelKlucza=Label(text="Wpisz klucz")
labelKlucza.pack()
entryDodawanyElement = Entry()
entryDodawanyElement.pack()
buttonDodEle = Button(text="Dodaj",command=dodawanieElementu)
buttonDodEle.pack()

def usuwanieKlucza():
    gq=str(usuwanieKluczaa.get())
    del slownik[gq]
    #l12.config(text="Usunoles klucz: " + str(gq))
    messagebox.showinfo("Usuniety klucz","Usunoles klucz: "+gq)
    labelSlownik.config(text="Twoj slownik to " + str(slownik))
    labelKluczeSlownika.config(text="Klucze w slowniku to: " + str(list(slownik.keys())))
usuwanieKluczaa = Entry()
usuwanieKluczaa.pack()
buttonUsuwanieKlucza = Button(text="Usun klucz",command=usuwanieKlucza)
buttonUsuwanieKlucza.pack()
# l12 = Label()
# l12.pack()
#Petle---------------------------------------------------------------------------------------------------#
l15=Label()
l15.pack()

titlesPetle = Label(text="Petle z zajec",bg='black',foreground='white')
titlesPetle.pack()

dodajZmiennaa = Entry()
globalnaLista=[]
gl=Label(text="Wpisz liczbe od 1 do 100")


def dodajElementtt():
    
    dodajZmienna = int(dodajZmiennaa.get())
    if dodajZmienna >= 1 and dodajZmienna <= 100:
        globalnaLista.append(dodajZmienna)
        #messagebox.showinfo("Dodales","Dodales liczbe: " + str(dodajZmienna))
        labelDodaj.config(text="Dodales element: " + str(dodajZmienna))
        #labelDodaj.config(text="Cała lista: " + str(globalnaLista))
        gl.config(text="Globalna lista: " + str(globalnaLista))
        #labeelUsun1.config(text="")
    elif dodajZmienna <= 1:
        labelDodaj.config(text="Podales za mala liczbe.") 
        gl.config(text="Globalna lista: " + str(globalnaLista))
        gl.config(text="Wpisz liczbe od 1 do 100")
    else:
        dodajZmienna >= 100
        labelDodaj.config(text="Podales za duza liczbe.") 
        gl.config(text="Globalna lista: " + str(globalnaLista))
        gl.config(text="Wpisz liczbe od 1 do 100")

gl.pack()
# labeelDodaj1 = Label()
# labeelDodaj1.pack()
dodajZmiennaa.pack()
buttonDodaj = Button(text="Dodaj",command=dodajElementtt)
buttonDodaj.pack()
labelDodaj = Label(text=globalnaLista)
labelDodaj.pack()
usunZmienna = Entry()
def usunElement():
    usunZmiennaa = int(usunZmienna.get())
    globalnaLista.remove(usunZmiennaa)
    labelDodaj.config(text="Usunoles element: " + str(usunZmiennaa))
    #labelUsun.config(text="Cała lista: " + str(globalnaLista))
    gl.config(text="Globalna lista: " + str(globalnaLista))
# labeelUsun1 = Label()
# labeelUsun1.pack()
usunZmienna.pack()
buttonUsun = Button(text="Usun liczbe",command=usunElement)
buttonUsun.pack()
# labelUsun = Label()
# labelUsun.pack()

# dodajEntr = Entry()
# dodajEntr.pack()
label2 = Label(text="Dodaj liczby z zakres:")
label2.pack()
drugaLiczba = Entry()
drugaLiczba.pack()
pierwszaLiczba = Entry()
pierwszaLiczba.pack()


def zadanie3():
    
    for n in range(int(drugaLiczba.get()),int(pierwszaLiczba.get())+1):
        #dodaj1 = int(dodajEntr.get())
        if n >= 1 and n <= 100:
            print(n)
            globalnaLista.append(n)
            gl.config(text="Globalna lista: " + str(globalnaLista))
#zadanie3()
print(globalnaLista)
dodajZakres = Button(text="Dodaj zakres",command=zadanie3)
dodajZakres.pack()

label2 = Label(text="Usun liczby z zakres:")
label2.pack()
drugaLiczba1 = Entry()
drugaLiczba1.pack()
pierwszaLiczba1 = Entry()
pierwszaLiczba1.pack()

def zadanie4():
    
    for n in range(int(drugaLiczba1.get()),int(pierwszaLiczba1.get())+1):
        #dodaj1 = int(dodajEntr.get())
        if n >= 1 and n <= 100:
            print(n)
            globalnaLista.remove(n)
            gl.config(text="Globalna lista: " + str(globalnaLista))
            
#zadanie3()
#print(globalnaLista)
usunZakres = Button(text="Usun zakres",command=zadanie4)
usunZakres.pack()

#Pliki---------------------------------------------------------------------------------------------------#
l15=Label()
l15.pack()
labelPlik = Label(text="Pliki",bg='black',foreground='white')
labelPlik.pack()
def tworzeniePliku():
    #a="cos"
    plik = open(str(entryNazwaPliku.get()) + ".txt","w",encoding="utf-8")
    #plik.write(a)
    labelStworzPlik.config(text="Stworzyles plik tekstowy o nazwie: " + str(entryNazwaPliku.get()))
    plik.write(str(entryTekstPliku.get()))
    stwplik = 'Stworzyles plik "' + str(entryNazwaPliku.get()) + '" z tekstem: "' + str(entryTekstPliku.get() + '"')
    messagebox.showinfo("Plik",stwplik)
    plik = open(str(entryNazwaPliku.get()) + ".txt","r")
    plik.read()
    plik.close()
labelStworzPlik = Label(text="Wpisz nazwe pliku jaki chcesz stworzyc")
labelStworzPlik.pack()
entryNazwaPliku = Entry()
entryNazwaPliku.pack()
labelTekstPliku = Label(text="Wpisz zawartosc jaka ma byc w pliku")
labelTekstPliku.pack()
entryTekstPliku = Entry()
entryTekstPliku.pack()
przycisk298 = Button(text="Plik2", command=tworzeniePliku)
przycisk298.pack()






okno.mainloop()

