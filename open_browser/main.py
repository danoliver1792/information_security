import webbrowser
from tkinter import *

# configuring Tkinter
root = Tk()
root.title("Open Browser")
root.geometry("300x200")


def google():
    """ function to open Google """
    webbrowser.open("www.google.com")


Button(root, text="Open Google", command=google).pack(pady=20)
root.mainloop()
