from tkinter import *
from tkinter import ttk
from app import MainUI

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
main_UI = MainUI(root)

root.mainloop()