import tkinter as tk
from tkinter import ttk

class ToolBarSeparator:

    def __init__(self, toolbar):
        self.toolbar = toolbar
        self.separator = ttk.Separator(self.toolbar, orient=tk.VERTICAL)
        self.separator.pack(side=tk.LEFT, fill=tk.Y, padx=4, pady=4)
