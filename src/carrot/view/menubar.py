import tkinter as tk

from .menu import Menu
from .menuitem import MenuItem

class MenuBar:

    def __init__(self, window):
        self.menubar = tk.Menu(window)
        window.config(menu=self.menubar)
        
        self.menu_file = Menu(self.menubar, "File")
        self.menu_file_exit = MenuItem(self.menu_file.menu, "Exit")
        
        self.menu_help = Menu(self.menubar, "Help")
        self.menu_help_about = MenuItem(self.menu_help.menu, "About")