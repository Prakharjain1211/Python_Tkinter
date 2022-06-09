from tkinter import *

root = Tk()

root.geometry('500x500')

f1 = Frame(root, bg='grey', borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y",pady=122)

f2 = Frame(root, bg='grey', borderwidth=6, relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l = Label(f1,text="Project Tkinter - Pycharm")
l.pack(pady=142)

l = Label(f2,text="Welcome to sublime text",font="Helvatica 16 bold",fg="red", pady=22)
l.pack()
root.mainloop()  