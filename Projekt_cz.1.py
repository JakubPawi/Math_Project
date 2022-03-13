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
frame.configure(background='#FFCCCC')
#topFrame = Frame(frame)
#topFrame.pack()
bottomFrame = Frame(frame)
bottomFrame.pack(side=BOTTOM)
#frame.geometry("400x300+200+200")
frame.geometry("900x1025+900+1")
my_scroll = Scrollbar(frame)
my_scroll.pack(side=RIGHT,fill=Y)

okno = Frame(frame)
okno.pack()

#Macierze---------------------------------------------------------------------------------------------------#

B = []
def GlobalnaLista():
             return B
def dodawanieDoTablicy():
    B.append(int(entryLiczbyMacierzy.get()))
    labelDoMacierzy.config(text="Twoja tablica:" + str(B))
    return B
liczbyMacierzy=Label(text="Podaj liczby macierzy od lewej do prawej",background='#FFCCCC')
liczbyMacierzy.pack()
entryLiczbyMacierzy = Entry()
entryLiczbyMacierzy.pack()
buttonDodawanieMa = Button(text="Dodaj do tablicy",command=dodawanieDoTablicy)
buttonDodawanieMa.pack()

def usuwanieElementu():
    for i in B[-1:]:
        B.remove(i)
        # print(i)
        # print(B)
        labelDoMacierzy.config(text="Twoja tablica:" + str(B))
    # B.remove(int(entryDoUsuwania.get()))
    #labelDoMacierzy.config(text="Twoja tablica:" + str(B))
buttonDoUsuwania = Button(text="Usuwanie ostatnio dodane", command=usuwanieElementu)
buttonDoUsuwania.pack()
  

def tworzenieMacierzy():
    C = np.array([B]).reshape(int(entryIloscWierszy.get()), int(entryIloscKolumn.get()))
    labelDoMacierzy.config(text="Twoja macierz to: \n"+ str(C))
    return C
labelDoMacierzy = Label(okno, text=(B),bg="lightblue")
labelDoMacierzy.pack(fill=X)
iloscWierszy=Label(text="Podaj ilość wierszy macierzy",background='#FFCCCC')
iloscWierszy.pack()
entryIloscWierszy = Entry()
entryIloscWierszy.pack()

iloscKolumn=Label(text="Podaj ilość kolumn macierzy",background='#FFCCCC')
iloscKolumn.pack()
entryIloscKolumn = Entry()
entryIloscKolumn.pack()

but = Button(text="Stworz macierz",command=tworzenieMacierzy)
but.pack()

def transponowanieMacierzy():
    C = np.array([B]).reshape(int(entryIloscWierszy.get()), int(entryIloscKolumn.get()))
    messagebox.showinfo("Transponowanie",str(C.T))
buttonDoTraM = Button(okno,text="Transponowanie", command=transponowanieMacierzy)
buttonDoTraM.pack(side = LEFT)

def rozmairMacierzy():
    C = np.array([B]).reshape(int(entryIloscWierszy.get()), int(entryIloscKolumn.get()))
    messagebox.showinfo("Liczba elementow",C.size)
buttonDoRozM22 = Button(okno,text="Wysiwtl liczbe elementow", command=rozmairMacierzy)
buttonDoRozM22.pack(side = LEFT)

def ksztaltMacierzy():
    C = np.array([B]).reshape(int(entryIloscWierszy.get()), int(entryIloscKolumn.get()))
    messagebox.showinfo("Wiersze i kolumny",C.shape)
buttonDoKszM22 = Button(okno,text="Wiersze i kolumny", command=ksztaltMacierzy)
buttonDoKszM22.pack(side = LEFT)

def wariancjarMacierzy():
    C = np.array([B]).reshape(int(entryIloscWierszy.get()), int(entryIloscKolumn.get()))
    gv=np.var(C)
    messagebox.showinfo("Wariancja",np.var(C))
buttonDoWarM22 = Button(okno,text="Wariancja", command=wariancjarMacierzy)
buttonDoWarM22.pack(side = LEFT)

def wymiaryMacierzy():
    C = np.array([B]).reshape(int(entryIloscWierszy.get()), int(entryIloscKolumn.get()))
    messagebox.showinfo("Liczba wymiarow",C.ndim)
buttonDoWymM22 = Button(okno,text="Liczba wymiarow", command=wymiaryMacierzy)
buttonDoWymM22.pack(side = LEFT)

def sredniaMacierzy():
    C = np.array([B]).reshape(int(entryIloscWierszy.get()), int(entryIloscKolumn.get()))
    messagebox.showinfo("Srednia wartosc",np.mean(C))
buttonDoSreM22 = Button(okno,text="Srednia wartosc", command=sredniaMacierzy)
buttonDoSreM22.pack(side = LEFT)

def odchylenieMacierzy():
    C = np.array([B]).reshape(int(entryIloscWierszy.get()), int(entryIloscKolumn.get()))
    messagebox.showinfo("Odchylenie",np.std(C))
buttonDoOdchM22 = Button(okno,text="Odchylenie", command=odchylenieMacierzy)
buttonDoOdchM22.pack(side = LEFT)
label=Label()
label.pack()

#Gra w losowanie---------------------------------------------------------------------------------------------------#
labelLosowanie=Label(text="GRA W LOSOWANIE",bg='black',foreground='white')
labelLosowanie.pack()
liczba = random.randint(1,100)
def sprawdz():
    
    x = int(e.get())
    if x > liczba:
        l.config(text="Moja liczba jest mniejsza")
    if x < liczba:
        l.config(text="Moja liczba jest wieksza")
    if x == liczba:
        l.config(text="Zgadles")

    print (liczba)

# def odnowa():

#     liczba = random.randint(1,100)
#     x = 0
#     l.config(text="Zgadnij")
#     print(liczba)
    
random.seed()

#liczba = random.randint(1,100)
#print (liczba)
x = 0
l1 = Label(text="Zgadnij liczbe",background='#FFCCCC')
l1.pack()
e = Entry(justify="center")
e.pack()
l = Label(text="")
l.pack()
przyc = Button(text="Sprawdz",command=sprawdz)
przyc.pack()
# przyc1 = Button(text="Od Nowa",command=odnowa)
# przyc1.pack()
label=Label()
label.pack()

#Krotka---------------------------------------------------------------------------------------------------#
labelKrotka=Label(text="KROTKA",bg='black',foreground='white')
labelKrotka.pack()
#gli = (1,2,3,'tekst',1)
#tak wiem, to troche oszukane :)
tablicaa = []
pustaKrotka = (tablicaa)

def tworzenieKrotki():
    if entryDodawanieKrotki.get() != ('') :
        tablicaa.append(str(entryDodawanieKrotki.get()))
        l8.config(text="Twoja krotka to: " + str(pustaKrotka))
    else:
        messagebox.showinfo("Blad","Wpisz cos :)")
entryDodawanieKrotki = Entry()
entryDodawanieKrotki.pack()
buttonTworzeniaKrotki = Button(text="Dodaj element krotki",command=tworzenieKrotki)
buttonTworzeniaKrotki.pack()

#def test1():
    #a = int(v.get())
    #r = str(v.get())
    #l8.config(text="Twoja krotka to "+str(gli))
def test2():
    a = int(v.get())
    r = str(v.get())
    l7.config(text='Twój element z pozycji "'+str(a)+'" to '+str(pustaKrotka[a]),bg='#FF99FF')
def test3():
    a = str(v.get())
    r = str(v.get())
    l7.config(text='Element "'+str(a)+'" wystepuje '+str(pustaKrotka.count(a)),bg='#FF9999')
l8=Label()
l8.pack()
v = Entry()
v.pack()
l7 = Label()
l7.pack()
# b1 = Button(text="Wyswietl krotke",command=test1)
# b1.pack()
b2 = Button(text="Element z pozycji",command=test2,bg='#FF99FF')
b2.pack()
b3 = Button(text="Ile razy wystepuje element",command=test3,bg='#FF9999')
b3.pack()
label=Label()
label.pack()

#Zbiory---------------------------------------------------------------------------------------------------#

zbiory=Label(text="ZBIORY",bg='black',foreground='white')
zbiory.pack()

analitycy={'Adam','Anna','Michał','Maria'}
programisci={'Adam','Tomasz','Krzysztof','Magdalena'}


def wyswietlAnalitykow():
    r = str(qwe.get())
    l11.config(text="Zbior analitykow: " + str(analitycy))
def wyswietlProgramistow():
    r = str(qwe.get())
    l111.config(text="Zbior programistow: " + str(programisci))
def zbio1():
    l12.config(text="ELement/y z obu zbiorow to: " + str(analitycy & programisci),bg='#77caa3')
def analitycyNieBedacyProgramistow():
    l12.config(text="Analitycy nie bedacy programistami: " + str(analitycy - programisci),bg='yellow')
def wszyscy():
    l12.config(text="Wszyscy: " + str(analitycy ^ programisci),bg='#66CCFF')
bo = Button(text="Wyswietl zbior analitykow",command=wyswietlAnalitykow)
bo.pack()
bo = Button(text="Wyswietl zbior programistow",command=wyswietlProgramistow)
bo.pack()
l11=Label()
l11.pack()
l111=Label()
l111.pack()
l12=Label()
l12.pack()
bo3 = Button(text="Wypisz wspolne element obu zbiorow",command=zbio1,bg='#77caa3')
bo3.pack()
bo4 = Button(text="Wypisz analitykow ktorzy nie sa programistami",command=analitycyNieBedacyProgramistow,bg='yellow')
bo4.pack()
bo4 = Button(text="Wypisz wszystkich ktorzy sa tylko raz",command=wszyscy,bg='#66CCFF')
bo4.pack()
def dodajAnalityka():
    r = str(qwe.get())
    analitycy.add(r)
    l13.config(text="Dodany analityk to " + str(r)+". Wszyscy: " + str(analitycy))
qwe = Entry()
qwe.pack() 
bo1 = Button(text="Dodaj analityka",command=dodajAnalityka)
bo1.pack()
l13 = Label()
l13.pack()

def dodajProgramiste():
    r = str(qwee.get())
    programisci.add(r)
    l13e.config(text="Dodany programista to " + str(r)+". Wszyscy: " + str(programisci))
qwee = Entry()
qwee.pack() 
bo1e = Button(text="Dodaj programiste",command=dodajProgramiste)
bo1e.pack()
l13e = Label()
l13e.pack()



okno.mainloop()

