
from tkinter import *
from tkinter import messagebox
from student.registerstudent import studreg
from studentcontrol import studcont


def register():
    studreg()


def slogin():
    
    def checkLogin():
        # data connection(login example)

        import mysql.connector  # step2

        # step3
        mydb = mysql.connector.connect(
            # host="localhost", #google.com---->12
            host="127.0.0.1",  # google.com---->12

            user="root",
            passwd="",
            database="examdb"
        )

        if mydb:
            print("Connection done")

            cur = mydb.cursor()  # step4

            qry = "SELECT *FROM student"  # step5
            name = enName.get()
            password = enpass.get()

            cur.execute(qry);  # step5
            # SELECT *FROM USERS WHERE NAME='KANTI';======>MYSQL ENGILNE===>TABLEUSER===KANTI(YES)
            rows = cur.fetchall()
            f = False
            for row in rows:
                if row[1] == name and row[2] == password:
                    f = True
                    studcont()
            if f == False:
                messagebox.showinfo('error', 'user name or password incorrect')
            mydb.close();

    mw = Tk()
    mw.geometry("300x300")
    name = Label(text="QUCK TEST")
    mw.configure(bg="olive")
    lblname = Label(mw, text="Enter name")
    enName = Entry(mw)
    lblpass = Label(mw, text="Password")
    enpass = Entry(mw)
    btn1=Button(mw,text="Register",command=register)
    btn2 = Button(mw, text="Login",command=checkLogin)
    lblname.place(x=20, y=50)
    lblpass.place(x=20, y=100)
    enName.place(x=150, y=50)
    enpass.place(x=150, y=100)
    btn1.place(x=100,y=200)
    btn2.place(x=200, y=200)
    mw.mainloop()