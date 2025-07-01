import tkinter as tk
from tkinter import messagebox

class MenuItem:

    def __init__(self, menu, text):
        self.menu = menu
        self.text = text

        if text == '-':
            self.menu.add_separator()
        else:
            self.menu.add_command(
                label=text,
                command=self._on_clicked
            )
    
    def _on_clicked(self):
        messagebox.showwarning( title="%s title" % (self.text), message="%s clicked" % (self.text) )