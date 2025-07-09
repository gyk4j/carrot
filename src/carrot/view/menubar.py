import tkinter as tk

from view.menu import Menu
from view.menuitem import MenuItem

class MenuBar:

    def __init__(self, window):
        self._window = window
        self._menubar = tk.Menu(window)
        self._window.config(menu=self._menubar)
        
        self._menu_file = Menu(self._menubar, "File")
        self._menu_file_new = MenuItem(self._menu_file.menu, "New")
        self._menu_file_open = MenuItem(self._menu_file.menu, "Open")
        self._menu_file_save = MenuItem(self._menu_file.menu, "Save")
        self._menu_file_saveas = MenuItem(self.menu_file.menu, "Save as")
        self._menu_file_separator = MenuItem(self._menu_file.menu, "-")
        self._menu_file_exit = MenuItem(self._menu_file.menu, "Exit")

        self._menu_go = Menu(self._menubar, "Go")
        self._menu_go_back = MenuItem(self._menu_go.menu, "Back")
        self._menu_go_next = MenuItem(self._menu_go.menu, "Next")
        
        self._menu_help = Menu(self._menubar, "Help")
        self._menu_help_about = MenuItem(self._menu_help.menu, "About")

    @property
    def window(self) -> tk.Toplevel:
        return self._window

    @window.setter
    def window(self, value: tk.Toplevel):
        self._window = value

    @property
    def menubar(self) -> tk.Menu:
        return self._menubar

    @menubar.setter
    def menubar(self, value: tk.Menu):
        self._menubar = value

    @property
    def menu_file(self) -> Menu:
        return self._menu_file

    @property
    def menu_file_new(self) -> MenuItem:
        return self._menu_file_new

    @property
    def menu_file_open(self) -> MenuItem:
        return self._menu_file_open

    @property
    def menu_file_save(self) -> MenuItem:
        return self._menu_file_save
    
    @property
    def menu_file_saveas(self) -> MenuItem:
        return self._menu_file_saveas

    @property
    def menu_file_exit(self) -> MenuItem:
        return self._menu_file_exit

    @property
    def menu_go(self) -> Menu:
        return self._menu_go

    @property
    def menu_go_back(self) -> MenuItem:
        return self._menu_go_back

    @property
    def menu_go_next(self) -> MenuItem:
        return self._menu_go_next

    @property
    def menu_help(self) -> Menu:
        return self._menu_help

    @property
    def menu_help_about(self) -> MenuItem:
        return self._menu_help_about