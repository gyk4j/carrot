from collections.abc import Callable

import tkinter as tk

# from tkinter import messagebox
# from tkinter import PhotoImage

from .tooltip import Tooltip
from controller.event import ActionEvent
from controller.event import ActionListener

class ToolBarButton:

    def __init__(self, toolbar, text='', icon='', onclick=None):
        # , action_listener: ActionListener
        self._text = text
        self._icon = icon
        self._image = tk.PhotoImage(file=self._icon)
        self._onclick = onclick
        self._button = tk.Button(
            toolbar,
            relief=tk.FLAT,
            #compound = tk.TOP,
            #text=self._text,
            command=self._onclick,
            image=self._image
        )
        self._tooltip = Tooltip(self._button, self._text)
        # self._action_listener = action_listener
        self._button.pack(side=tk.LEFT, padx=0, pady=0)
    
    @property
    def toolbar(self) -> tk.Frame:
        return self._toolbar

    @toolbar.setter
    def toolbar(self, value: tk.Frame):
        self._toolbar = value 

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
    def onclick(self) -> Callable:
        return self._onclick

    @onclick.setter
    def onclick(self, value: Callable):
        self._onclick = value
        self._button.configure(command=self._onclick)
        
    