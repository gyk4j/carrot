import tkinter as tk

from .menu import Menu
from .menuitem import MenuItem

from ..resource import ClassLoader

class MenuBar:

    def __init__(self, window):
        self._window = window
        self._menubar = tk.Menu(window)
        self._window.config(menu=self._menubar)

        cl = ClassLoader()
        
        self._menu_file = Menu(self._menubar, "File")
        self._menu_file_new = MenuItem(self._menu_file.menu, "New", cl.get_resource("res/ico/file_new_24.png"), 'Ctrl+N')
        self._menu_file_open = MenuItem(self._menu_file.menu, "Open", cl.get_resource("res/ico/file_open_24.png"), 'Ctrl+O')
        self._menu_file_save = MenuItem(self._menu_file.menu, "Save", cl.get_resource("res/ico/file_save_24.png"), 'Ctrl+S')
        self._menu_file_saveas = MenuItem(self.menu_file.menu, "Save as", cl.get_resource("res/ico/file_saveas_24.png"), 'Ctrl+Shift+S')
        self._menu_file_separator1 = MenuItem(self._menu_file.menu, "-")
        self._menu_file_export = MenuItem(self.menu_file.menu, "Export", cl.get_resource("res/ico/file_export_24.png"), 'Ctrl+Alt+E')
        self._menu_file_separator2 = MenuItem(self._menu_file.menu, "-")
        self._menu_file_exit = MenuItem(self._menu_file.menu, "Exit", cl.get_resource("res/ico/file_exit_24.png"))

        self._menu_go = Menu(self._menubar, "Go")
        self._menu_go_back = MenuItem(self._menu_go.menu, "Back", cl.get_resource("res/ico/go_back_24.png"), 'Alt+Left')
        self._menu_go_next = MenuItem(self._menu_go.menu, "Next", cl.get_resource("res/ico/go_forward_24.png"), 'Alt+Right')

        self._menu_selection = Menu(self._menubar, "Selection")
        self._menu_selection_contract = MenuItem(self._menu_selection.menu, "Contract", cl.get_resource("res/ico/selection_contract_24.png"), 'Ctrl+-')
        self._menu_selection_expand = MenuItem(self._menu_selection.menu, "Expand", cl.get_resource("res/ico/selection_expand_24.png"), 'Ctrl++')
        self._menu_file_separator3 = MenuItem(self._menu_selection.menu, "-")
        self._menu_selection_mark = MenuItem(self._menu_selection.menu, "Mark", cl.get_resource("res/ico/selection_mark_24.png"), 'Enter')
        
        self._menu_help = Menu(self._menubar, "Help")
        self._menu_help_view = MenuItem(self._menu_help.menu, "View Help", cl.get_resource("res/ico/help_view_24.png"), 'F1')
        self._menu_file_separator4 = MenuItem(self._menu_help.menu, "-")
        self._menu_help_about = MenuItem(self._menu_help.menu, "About Carrot", cl.get_resource("res/ico/help_about_24.png"))

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
    def menu_file_export(self) -> MenuItem:
        return self._menu_file_export

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
    def menu_selection(self) -> Menu:
        return self._menu_selection

    @property
    def menu_selection_contract(self) -> MenuItem:
        return self._menu_selection_contract

    @property
    def menu_selection_expand(self) -> MenuItem:
        return self._menu_selection_expand

    @property
    def menu_selection_mark(self) -> MenuItem:
        return self._menu_selection_mark

    @property
    def menu_help(self) -> Menu:
        return self._menu_help

    @property
    def menu_help_view(self) -> MenuItem:
        return self._menu_help_view

    @property
    def menu_help_about(self) -> MenuItem:
        return self._menu_help_about