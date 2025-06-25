import tkinter as tk

class StatusBarPane:

    def __init__(self, statusbar, fill):
        self.statusbar = statusbar
        self.text = ''
        self.statusbarpane = tk.Label(
            self.statusbar,
            text='',
            justify=tk.LEFT,
            anchor=tk.W,
            relief=tk.SUNKEN,
            borderwidth = 1,
            padx = 4,
            pady = 2,
        )
        
        if fill is True:
            self.statusbarpane.pack(side=tk.LEFT, padx=1, pady=1, expand=True, fill=tk.X)
        else:
            self.statusbarpane.pack(side=tk.LEFT, padx=1, pady=1)
    
    def set_text(self, text):
        self.text = text
        self.statusbarpane['text'] = self.text