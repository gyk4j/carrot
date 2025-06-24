import tkinter as tk

from .statusbarpane import StatusBarPane

class StatusBar:

    def __init__(self, window):
        self.statusbar = tk.Frame(window)
        
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.file = StatusBarPane(self.statusbar, True)
        self.progress = StatusBarPane(self.statusbar, False)
        self.mouse = StatusBarPane(self.statusbar, False)
        self.selection = StatusBarPane(self.statusbar, False)
        
        self.file.set_text('C:\Windows')
        self.progress.set_text('1 / 999')
        self.mouse.set_text("%d, %d" % (123, 456))
        self.selection.set_text("%d x %d pixels" % (300, 600))
        