import tkinter as tk

class StatusBarPane:

    def __init__(self, statusbar, fill):
        self._statusbar = statusbar
        self._text = ''
        self._statusbarpane = tk.Label(
            self._statusbar,
            text='',
            justify=tk.LEFT,
            anchor=tk.W,
            relief=tk.SUNKEN,
            borderwidth = 1,
            padx = 4,
            pady = 2
        )
        
        if fill is True:
            self._statusbarpane.pack(side=tk.LEFT, padx=1, pady=1, expand=True, fill=tk.X)
        else:
            self._statusbarpane.pack(side=tk.LEFT, padx=1, pady=1)

    @property
    def statusbar(self) -> tk.Frame:
        return self._statusbar

    @property
    def statusbarpane(self) -> tk.Label:
        return self._statusbarpane

    def set_text(self, text):
        self._text = text
        self._statusbarpane['text'] = self._text
