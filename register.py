import mysql.connector as mysqlconnector
import tkinter as mytk
from tkinter import *
import tkinter.messagebox as mymessagebox

MyLoginForm1 = mytk.Tk()
MyLoginForm1.title('Login Form with MYSQL Connection')
# Set Form Size
MyLoginForm1.geometry("1500x1000")


def Clicktoregister():
    mydb = mysqlconnector.connect(host="localhost", user="root", password="saianshika2020!", database="database2")
    mycursor = mydb.cursor()

    mycursor.execute("INSERT INTO register VALUES (%s,%s,%s,%s,%s)",
                     (
                         FNLabelTxt.get(),
                         LNLabelTxt.get(),
                         emailLabelTxt.get(),
                         PassTxt.get(),
                         PwdTxt.get()
                     )
                     )

    if FNLabelTxt.get() == "" or LNLabelTxt.get() == "" or emailLabelTxt.get() == "" or PassTxt.get() == "" or PwdTxt.get() == "":
        mymessagebox.showerror("Error", 'Enter all fields')

    elif PassTxt.get() != PwdTxt.get():
        mymessagebox.showerror("Error", 'password and confirm password should be same')

    else:
        mymessagebox.showerror("successfully registered")
    mycursor.close()
    # sql.close()
    mydb.commit()
    mydb.close()

    # **********HEADING LABEL***********


Bannerlabel = Label(MyLoginForm1, text=" USER REGISTRATION......", width=40, bg='yellow')
Bannerlabel.place(x=200, y=100)

# ****************FIRSTNAME***************
FNLabel = Label(MyLoginForm1, text="FIRSTNAME", width=10)
FNLabel.place(x=120, y=260)

FNLabelTxt = Entry(MyLoginForm1, width=27, relief="flat")
FNLabelTxt.place(x=250, y=260)

FNLabelTxt.focus()

# *************LASTANME********************
LNLabel = Label(MyLoginForm1, text="LASTNAME", width=10)
LNLabel.place(x=120, y=290)

LNLabelTxt = Entry(MyLoginForm1, width=27, relief="flat")
LNLabelTxt.place(x=250, y=290)

# LNLabelTxt.focus()

# ****************EMAIL********************

emailLabel = Label(MyLoginForm1, text="EMail", width=10)
emailLabel.place(x=120, y=320)

emailLabelTxt = Entry(MyLoginForm1, width=27, relief="flat")
emailLabelTxt.place(x=250, y=320)

# emailLabelTxt.focus()

# **************PASSWORD******************
PassLabel = Label(MyLoginForm1, text="Password ", width=10)
PassLabel.place(x=120, y=350)

PassTxt = Entry(MyLoginForm1, width=27, relief="flat")
PassTxt.place(x=250, y=350)

# Set Password Char in Entry Widget
PassTxt.config(show="*")

# *************CONFIRM PASSWORD******************
PwdLabel = Label(MyLoginForm1, text="confirm Password :", width=10)
PwdLabel.place(x=120, y=400)

PwdTxt = Entry(MyLoginForm1, width=27, relief="flat")
PwdTxt.place(x=250, y=400)

# Set Password Char in Entry Widget
PwdTxt.config(show="*")

LoginBtn = Button(MyLoginForm1, text="submit", command=Clicktoregister, relief="groove", fg='blue')
LoginBtn.place(x=400, y=540)

MyLoginForm1.configure(background='#54596d')
MyLoginForm1.mainloop()
