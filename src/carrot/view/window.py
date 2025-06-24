import tkinter as tk
from tkinter import messagebox

from .menubar import MenuBar
from .toolbar import ToolBar
from .statusbar import StatusBar

class Window:

    def __init__(self, title):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry("%dx%d" % (1024, 640))
        
        # Add menu bar
        self.menubar = MenuBar(self.window)
        
        # Add tool bar
        self.toolbar = ToolBar(self.window)
        
        # Add status bar
        self.statusbar = StatusBar(self.window)
    
    def show(self):
        # Center the window
        # https://www.geeksforgeeks.org/python/how-to-center-a-window-on-the-screen-in-tkinter/
        self.window.update_idletasks()
        
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2 - 48
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        
        self.window.mainloop()
