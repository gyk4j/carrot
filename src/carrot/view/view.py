import tkinter as tk

def info(title='', message=''):
    tk.messagebox.showinfo(title = title, message = message)

def warn(title='', message=''):
    tk.messagebox.showwarning(title = title, message = message)

def error(title='', message=''):
    tk.messagebox.showerror(title = title, message = message)
