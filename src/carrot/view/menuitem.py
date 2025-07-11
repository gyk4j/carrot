from collections.abc import Callable

import tkinter as tk
from tkinter import messagebox

class MenuItem:

    def __init__(self, menu, text='', icon='', accelerator='', onclick=None):
        self._menu : tk.Menu = menu
        self._text : str = text
        self._icon : str = icon

        # Icon is optional
        if self._icon == '':
            self._image = None
        else:
            self._image = tk.PhotoImage(file=self._icon)

        # Accelerator is optional
        self._accelerator = accelerator

        self._onclick = onclick

        if self._text == '-':
            self._menu.add_separator()
        elif self._onclick is None:
            self._menu.add_command(
                label=self._text,
                image=self._image,
                compound=tk.LEFT,
                accelerator=self._accelerator,
            )
        else:
            self._menu.add_command(
                label=self._text,
                image=self._image,
                compound=tk.LEFT,
                accelerator=self._accelerator,
                command=self._onclick
            )
    
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

    @property
    def icon(self) -> str:
        return self._icon

    @icon.setter
    def icon(self, value: str):
        self._icon = value
    
    @property
    def image(self) -> tk.PhotoImage:
        return self._image

    @image.setter
    def image(self, value: tk.PhotoImage):
        self._image = value

    @property
    def accelerator(self) -> str:
        return self._accelerator

    @accelerator.setter
    def accelerator(self, value: str):
        self._accelerator = value
        self._menu.entryconfigure(self._text, accelerator=self._accelerator)

    @property
    def onclick(self) -> Callable:
        return self._onclick

    @onclick.setter
    def onclick(self, value: Callable):
        self._onclick = value
        self._menu.entryconfigure(self._text, command=self._onclick)