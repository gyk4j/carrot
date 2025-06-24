import tkinter as tk

from .toolbarbutton import ToolBarButton

class ToolBar:

    def __init__(self, window):
        self.toolbar = tk.Frame(window)
        #(borderwidth = 2, relief=tk.RAISED)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
        
        self.file_new = ToolBarButton(self.toolbar, "New", "res/ico/file_new.png")
        self.file_open = ToolBarButton(self.toolbar, "Open", "res/ico/file_open.png")
        self.file_save = ToolBarButton(self.toolbar, "Save", "res/ico/file_save.png")
        self.file_saveas = ToolBarButton(self.toolbar, "Save as", "res/ico/file_saveas.png")
        self.file_exit = ToolBarButton(self.toolbar, "Exit", "res/ico/file_exit.png")