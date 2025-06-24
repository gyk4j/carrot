import tkinter as tk

from tkinter import messagebox
from tkinter import PhotoImage

from .tooltip import Tooltip

class ToolBarButton:

    def __init__(self, toolbar, text, icon):
        self.text = text
        self.icon = icon
        self.image = PhotoImage(file=self.icon)
        self.button = tk.Button(
            toolbar,
            relief=tk.FLAT,
            #compound = tk.TOP,
            #text=self.text,
            command=self._on_clicked,
            image=self.image
        )
        self.tooltip = Tooltip(self.button, self.text)
        self.button.pack(side=tk.LEFT, padx=0, pady=0)    
        
    def _on_clicked(self):
        messagebox.showinfo( title="%s title" % (self.text), message="%s clicked" % (self.text))