import tkinter as tk

from .menu import Menu
from .menuitem import MenuItem

class MenuBar:

    def __init__(self, window):
        self.menubar = tk.Menu(window)
        window.config(menu=self.menubar)
        
        self.menu_file = Menu(self.menubar, "File")
        self.menu_file_new = MenuItem(self.menu_file.menu, "New")
        self.menu_file_open = MenuItem(self.menu_file.menu, "Open")
        self.menu_file_save = MenuItem(self.menu_file.menu, "Save")
        self.menu_file_saveas = MenuItem(self.menu_file.menu, "Save as")
        self.menu_file_separator = MenuItem(self.menu_file.menu, "-")
        self.menu_file_exit = MenuItem(self.menu_file.menu, "Exit")

        self.menu_go = Menu(self.menubar, "Go")
        self.menu_go_back = MenuItem(self.menu_go.menu, "Back")
        self.menu_go_next = MenuItem(self.menu_go.menu, "Next")
        
        self.menu_help = Menu(self.menubar, "Help")
        self.menu_help_about = MenuItem(self.menu_help.menu, "About")