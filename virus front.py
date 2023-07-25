import keyboard
from tkinter import *


def window():
    win = Tk()
    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()
    win.overrideredirect(True)
    win.wm_attributes('-topmost', 1)
    canvas = Canvas(win, width=width, height=height)
    canvas.pack()
    win.mainloop()

    keyboard.add_hotkey('alt+a', window())

if __name__ == '__main__':
    window()