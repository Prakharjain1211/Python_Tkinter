from tkinter import *

def getvals():
    print(f"Your username is {uservalue.get()}")
    print(f"Your password is {passvalue.get()}")
root = Tk()
root.geometry('655x333')

user= Label(root, text="Username")
pas= Label(root, text="Passsword")
user.grid()
pas.grid(row=1)

#variable classes in tkinter
# BolleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable= uservalue)
passentry = Entry(root, textvariable= passvalue)

userentry.grid(row = 0, column = 1)
passentry.grid(row = 1, column = 1)

Button(text="Submit", command=getvals).grid()

root.mainloop() 