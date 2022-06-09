from tkinter import *
from PIL import Image
from PIL import ImageTk

root = Tk()

# photo = PhotoImage(file = "1.png")

# Apart form images

image = Image.open("1.webp")
photo = ImageTk.PhotoImage(image)

lab = Label(image=photo)

lab.pack()

root.mainloop()