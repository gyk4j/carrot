import tkinter as tk

from .menuitem import MenuItem

class Menu:

    def __init__(self, menubar, text):
        self.menubar = menubar
        self.text = text
        
        self.menu = tk.Menu(menubar, tearoff=False)
        
        self.menubar.add_cascade(
            label=self.text,
            menu=self.menu
        )

        
    