from tkinter import *
from tkinter import messagebox
import tkinter as tk
def hesapla(tur):
    if i1.get()=="" and i2.get()=="":
        #messagebox.showinfo("Uyarı" , "Veri Girmediniz :(")
        islem.configure(text="Veri Girmediniz")
        i1.delete(0, END)
        i2.delete(0, END)
        i1.focus()
    elif i1.get().isdigit() and i2.get().isdigit():
        s1=float(i1.get())
        s2=float(i2.get())
        if(tur=="+"):
            islem.configure(text=str(s1+s2))
        elif(tur=="-"):
            islem.configure(text=str(s1-s2))
        elif(tur=="*"):
            islem.configure(text=str(s1*s2))
        elif(tur=="/"):
           islem.configure(text=str(s1/s2))
    else:
        #messagebox.showinfo("Uyarı" , "Hatalı veri girdiniz :(")
        islem.configure(text="Hatalı veri girdiniz!")
        i1.delete(0, END)
        i2.delete(0, END)
        i1.focus()
           
def topla():
    hesapla("+")        

def fark():
      hesapla("-")     

def carp():
      hesapla("*")
      
def bol():
      hesapla("/")

    
pencere=Tk()
pencere.title('Dört İşlem V 1.0')
pencere.geometry("500x500")
pencere.configure(bg="yellow")
pencere.resizable(False,False)

e1=Label(pencere,text="1. Sayıyı Giriniz:")
e1['bg'] = pencere['bg']
e1.place(x=20,y=10)
e2=Label(pencere,text="2. Sayıyı Giriniz:")
e2['bg'] = pencere['bg']
e2.place(x=20,y=40)
i1 = Entry(pencere, bd =2)
i1.place(x=150, y=10)
i2 = Entry(pencere, bd =2)
i2.place(x=150, y=40)
sonuc=Label(pencere,text="Sonuç:")
sonuc['bg'] = pencere['bg']
sonuc.place(x=20,y=70)
islem=Label(pencere,text="...",font="Courier 16 bold", justify="center")
islem['bg'] = pencere['bg']
islem.place(x=150,y=70)
btn1 = tk.Button(pencere, text="+", font="Courier 12 bold", width=4,command=topla)
btn1.place(x=100, y=110)
btn2 = tk.Button(pencere, text="-", font="Courier 12 bold", width=4,command=fark)
btn2.place(x=150, y=110)
btn3 = tk.Button(pencere, text="*", font="Courier 12 bold", width=4, command=carp)
btn3.place(x=200, y=110)
btn4 = tk.Button(pencere, text="/", font="Courier 12 bold", width=4,command=bol)
btn4.place(x=250, y=110)
i1.focus()
pencere.mainloop()
