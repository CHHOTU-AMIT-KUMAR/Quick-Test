from tkinter import*
from tkinter.ttk import*
from admpass import changepasw
def changep():
    changepasw()

def admincont():

   
    mw=Tk()
    mw.title("Quick Test")
    mw.geometry("300x300")
    mw.configure(bg="gray")

    menubar=Menu(mw)
    passmenu=Menu(menubar,tearoff=0)
    passmenu.add_command(label="changepass",command=changep)
    passmenu.add_separator()
    passmenu.add_command(label="Exit",command=mw.quit)
    menubar.add_cascade(label="password",menu=passmenu)

    
    objmenu=Menu(menubar,tearoff=0)
    objmenu.add_command(label="Add")
    objmenu.add_command(label="Update")
    objmenu.add_command(label="Remove")
    menubar.add_cascade(label="Objques",menu=objmenu)


    subjmenu=Menu(menubar,tearoff=0)
    subjmenu.add_command(label="Add")
    subjmenu.add_command(label="Update")
    subjmenu.add_command(label="Remove")
    menubar.add_cascade(label="Subjques",menu=subjmenu)


    student=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Student",menu=student)
    mw.config(menu=menubar)
    mw.mainloop()




