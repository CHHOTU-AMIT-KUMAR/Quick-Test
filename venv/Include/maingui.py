from tkinter.ttk import*
from tkinter import*
import tkinter.font as font
from adminlogin import login
from studentlogin import slogin



def calladmlogin():
    login()
    mw.destroy()
def callstulogin():
    slogin()
    mw.destroy()
mw=Tk()
mw.geometry("300x300")

mw.title("Qick Test")
myFont = font.Font(family='Helvetica', size=20, weight='bold')
mw.configure(bg="pink")
name=Label(text="QUCK TEST")
name['font']=myFont
btn1=Button(mw,text="ADMIN",command=calladmlogin)
btn2=Button(mw,text="STUDENT",command=callstulogin)
name.pack()

btn1.place(x="130",y="100")
btn2.place(x="130",y="200")
mw.mainloop()