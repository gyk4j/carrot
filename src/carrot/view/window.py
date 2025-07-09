import tkinter as tk
from tkinter import messagebox

from .menubar import MenuBar
from .toolbar import ToolBar
from .imageview import ImageView
from .statusbar import StatusBar

class Window:

    DEFAULT_WIDTH = 1024
    DEFAULT_HEIGHT = 640

    def __init__(self, title):
        self._window = tk.Tk()
        self._window.title(title)
        self._window.geometry("%dx%d" % (Window.DEFAULT_WIDTH, Window.DEFAULT_HEIGHT))
        self._window.config(bg="black")
        
        # Add menu bar
        self._menubar = MenuBar(self.window)
        
        # Add tool bar
        self._toolbar = ToolBar(self.window)

        # Add image view
        self._imageview = ImageView(self.window)
        
        # Add status bar
        self._statusbar = StatusBar(self.window)

    @property
    def window(self) -> tk.Toplevel:
        return self._window

    @property
    def menubar(self) -> MenuBar:
        return self._menubar

    @property
    def toolbar(self) -> ToolBar:
        return self._toolbar

    @property
    def imageview(self) -> ImageView:
        return self._imageview

    @property
    def statusbar(self) -> StatusBar:
        return self._statusbar

    def show(self):
        # Center the window
        # https://www.geeksforgeeks.org/python/how-to-center-a-window-on-the-screen-in-tkinter/
        self._window.update_idletasks()
        
        #window_width = Window.DEFAULT_WIDTH
        window_width = self._window.winfo_width()
        #window_height = Window.DEFAULT_HEIGHT
        window_height = self._window.winfo_height()
        screen_width = self._window.winfo_screenwidth()
        screen_height = self._window.winfo_screenheight()
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2 - 48 # Shift up by 48 pixels for taskbar.
        self._window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        self.window.mainloop()

    def notify(self, title='lorem', message='ipsum'):
        tk.messagebox.showinfo(title = title, message = message)

