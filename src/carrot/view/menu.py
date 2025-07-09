import tkinter as tk

class Menu:

    def __init__(self, menubar, text):
        self._menubar = menubar
        self._text = text
        
        self._menu = tk.Menu(self._menubar, tearoff=False)
        
        self._menubar.add_cascade(
            label=self._text,
            menu=self._menu
        )

    @property
    def menubar(self) -> tk.Menu:
        return self._menubar

    @menubar.setter
    def menubar(self, value: tk.Menu):
        self._menubar = value

    @property
    def menu(self) -> tk.Menu:
        return self._menu

    @menu.setter
    def menu(self, value: tk.Menu):
        self._menu = value

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str):
        self._text = value
        
    