from tkinter import*
import tkinter.font as font
from studpass import cstudpass

def cstud():
    cstudpass()
def studcont():
    mw = Tk()
    mw.title("Quick Test")
    mw.geometry("300x300")
    mw.configure(bg="purple")
    myFont = font.Font(family='Helvetica', size=20, weight='bold')
    name =Label(mw,text="QUCK TEST")
    name['font'] = myFont
    btn1=Button(mw,text="changepassword",command=cstud)
    btn2=Button(mw,text="ShowPaper")
    name.pack()
    btn1.place(x=105, y=180)
    btn2.place(x=120, y=100)
    mw.mainloop()





