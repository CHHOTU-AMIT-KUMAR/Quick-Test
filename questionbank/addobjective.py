from tkinter import *
from tkinter import ttk
import tkinter.font as font
import mysql.connector
def addobj():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="examdb"
    )
    curs = mydb.cursor()
    curs.execute('select subjectname from subject')
    results = curs.fetchall()
    combobox = [result[0] for result in results]
    def LookUp(*args):
        cursor = mydb.cursor()
        option = cb1.get()
        query = "SELECT *FROM subject WHERE subjectname=%s"
        cursor.execute(query, (option,))
        rows = cursor.fetchall()
        for i in rows:
            subid = i[0]
        query2 = "SELECT *FROM topic WHERE subjectid = %s"
        cursor.execute(query2, (subid,))
        rows1 = cursor.fetchall()
        mylist = [j[1] for j in rows1]
        cb2['value'] = mylist

    mw = Tk()
    mw.title("Add Objective")
    myFont = font.Font(family='Helvetica', size=20, weight='bold')
    name = Label(text="ADD QUESTION ?")
    name['font'] = myFont
    mw.configure(bg="olive")
    mw.geometry("400x400")
    name.pack()
    cb1 = ttk.Combobox(mw,value=combobox, width=15, font=("arial ", 12))
    cb1.place(x=40,y=150)
    cb2 = ttk.Combobox(mw, width=15, font=("arial ", 12))
    cb2.place(x=200, y=150)
    cb1.bind("<<ComboboxSelected>>",LookUp)
    mw.mainloop()
addobj()