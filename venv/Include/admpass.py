from tkinter import*
from tkinter import messagebox
import mysql.connector

def changepasw():
    def update():
        mydb = mysql.connector.connect(
            # host="localhost", #google.com---->12
            host="127.0.0.1",  # google.com---->12

            user="root",
            password="",
            database="examdb"
        )

        if mydb:
            print("Connection done")

            cur = mydb.cursor();  # step4

            qry = "UPDATE admin set password= %s "  # step5


            password = enpass.get()
            tpval = (password,)

            cur.execute(qry, tpval)  # step5
            mydb.commit()
            res = Message(text="Done")
            mydb.close();
    mk=Tk()
    mk.geometry("300x300")
    mk.title("QuickTest")
    mk.configure(bg="gray")
    pasw =Label(mk,text= "Enter new Password:")
    enpass = Entry(mk)
    btn=Button(mk, text="Change",command=update)
    pasw.place(x=30, y=150)
    enpass.place(x=150, y=150)
    btn.place(x=220, y=200)
    mk.mainloop()