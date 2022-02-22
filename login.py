import mysql.connector as mysqlconnector
import tkinter as mytk
from tkinter import *
import tkinter.messagebox as mymessagebox

MyLoginForm = mytk.Tk()
MyLoginForm.title('Login Form with MYSQL Connection')
# Set Form Size
MyLoginForm.geometry("1500x1000")


def Clicktorlogin():

    mydb = mysqlconnector.connect(host="localhost", user="root", password="saianshika2020!", database="database2")

    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute(
        "SELECT * FROM register where email = '" + UserTxt.get() + "' and password = '" + PassTxt.get() + "';")
    myresult = mycursor.fetchone()
    if UserTxt.get() == "" or  PassTxt.get() == "":
        mymessagebox.showerror("Error","fields cant be empty")

    elif myresult == None:
        mymessagebox.showerror("Error", "Enter correct User Name And Password")

    else:
        mymessagebox.showinfo("Success", "Successfully Login")

    mycursor.close()
    mydb.close()

    # **********HEADING LABEL***********


Bannerlabel = Label(MyLoginForm, text="Email Login Form......", width=40, bg='yellow')
Bannerlabel.place(x=200, y=100)

# ****************FIRSTNAME***************

UserLabel = Label(MyLoginForm, text="Enter Email:", width=10)
UserLabel.place(x=120, y=260)

UserTxt = Entry(MyLoginForm, width=27, relief="flat")
UserTxt.place(x=230, y=260)

UserTxt.focus()

# *************LASTANME********************
PassLabel = Label(MyLoginForm, text="Enter Password :", width=10)
PassLabel.place(x=120, y=290)

PassTxt = Entry(MyLoginForm, width=27, relief="flat")
PassTxt.place(x=230, y=290)

PassTxt.config(show="*")

LoginBtn = Button(MyLoginForm, text="Login", command=Clicktorlogin, relief="groove", fg='blue')
LoginBtn.place(x=300, y=340)

register = Button(MyLoginForm, text="click to Register", relief="groove", fg='blue')
register.place(x=400, y=340)

forgotpassword = Button(MyLoginForm, text="forgotpassword", relief="groove", fg='blue')
forgotpassword.place(x=550, y=340)

MyLoginForm.configure(background='#54596d')
MyLoginForm.mainloop()
