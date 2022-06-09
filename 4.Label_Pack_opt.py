import imp
from ssl import Options
from textwrap import fill
import tkinter

from tkinter import *
from turtle import left, right

root  = Tk()

root.geometry("444x333")
root.title("My Gui With Prakhar")

# Important label Options

# text = adds the text
# bd = bakchground
# fg = foreground

# font = sets the fonts
# 1. font= ("comicsansms",19, SUNKEN)
# 2. font= "comicsansms",19, SUNKEN"

# padx = x padding
# pady = y padding
# relief = border styling = SUNKEn, RAUSED, GROOVE, RIDGE

title_label = Label(text ='''Lorem Ipsum is simply dummy text of the printing and typesetting
 industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
 when an unknown printer took a galley of type and scrambled it to make a type specimen 
 book. It has survived not only five centuries, but also the leap into electronic 
 typesetting, remaining essentially unchanged. It was popularised in the 1960s with the 
 release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop 
 publishing software like Aldus PageMaker including versions of Lorem Ipsum.''', bg="red", fg='white', padx=113, pady=94, font="comicsansms 19 bold", borderwidth=3, relief=SUNKEN )


#  Important Pack Options
# anchor = nw, sw,etc.
# side = top, down, left , right
# fill
# padx
# pady


# title_label.pack(side =BOTTOM ,anchor="sw",fill=X)
title_label.pack(side =LEFT ,fill=Y, padx=34, pady=34)

root.mainloop()