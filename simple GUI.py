from tkinter import *
from tkinter import ttk

root = Tk()

frm = ttk.Frame(root, padding=50)
frm.grid()

ttk.Label(frm, text="Gusto ko na matapos").grid(column=0, row=0)

ttk.Button(frm, text="Sige", command=root.destroy).grid(column=1, row=0)

root.mainloop()
