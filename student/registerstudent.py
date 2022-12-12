from tkinter import*
from tkinter import messagebox
import mysql.connector


def studreg():

    def insertstudent():
        mydb = mysql.connector.connect(
            # host="localhost",#google.com-->12
            host="127.0.0.1",  # google.com--->12
            user="root",
            password="",
            database="examdb"
        )
        if mydb:
            print("connection done")
            cur = mydb.cursor()

            qry = "insert into student(name,password,email,collegename,branch,mobile,age) values(%s,%s,%s,%s,%s,%s,%s)";
            name = enName.get()
            # console ===>input("enter user name")
            # input==>GUI
            password = enPass.get()
            email =eneml.get()
            collegname  =enclg.get()
            branch =enbranch.get()
            mobile =enmbl.get()
            age =enage.get()

            tpval = (name, password, email, collegname, branch, mobile, age)
            cur.execute(qry, tpval)  # use cursor predefined function
            # (prepare)insert into user(name,password)values(sushil,1234)
            mydb.commit()
            messagebox.showinfo("insert info", name + "rows inserted")
            mydb.close()
    mw = Tk()
    mw.geometry("400x400")
    mw.title("Quick Register")
    mw.configure(bg="gray")
    lblname = Label(mw, text="Enter Name:")
    lblpass = Label(mw, text="Enter Password")
    lblage = Label(mw, text="Enter Age")
    lblmbl = Label(mw, text="Enter Mobile")
    lbleml = Label(mw, text="Enter Email:")
    lblclg = Label(mw, text="Enter college Name: ")
    lblbranch = Label(mw, text="Enter Branch:")
    enName = Entry(mw)
    enPass = Entry(mw)
    enage = Entry(mw)
    enmbl = Entry(mw)
    eneml = Entry(mw)
    enclg = Entry(mw)
    enbranch = Entry(mw)
    btn1 = Button(mw, text="Back")
    btn2 = Button(mw, text="Save",command=insertstudent)
    lblname.place(x=50, y=40)
    enName.place(x=180, y=40)
    lblpass.place(x=50, y=80)
    enPass.place(x=180, y=80)
    lbleml.place(x=50, y=120)
    eneml.place(x=180, y=120)
    lblclg.place(x=50, y=160)
    enclg.place(x=180, y=160)
    lblbranch.place(x=50, y=200)
    enbranch.place(x=180, y=200)
    lblmbl.place(x=50, y=240)
    enmbl.place(x=180, y=240)
    lblage.place(x=50, y=280)
    enage.place(x=180, y=280)
    btn1.place(x=150, y=350)
    btn2.place(x=200, y=350)

    mw.mainloop()













