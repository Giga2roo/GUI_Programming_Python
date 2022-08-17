# import
import tkinter as tk
from tkinter import ttk

# create instance
win = tk.Tk()

# adding a Label
win.title("Python GUI")

# Adding a Label
ttk.Label(win, text="Yeah!!!").grid(column=0, row=0)

# start GUI
win.mainloop()