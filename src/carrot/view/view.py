import tkinter as tk
from tkinter import messagebox

class Window:

    def __init__(self, title):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry("%dx%d" % (1024, 640))
        
        # Add menu bar
        menubar = MenuBar(self.window)
    
    def show(self):
        # Center the window
        # https://www.geeksforgeeks.org/python/how-to-center-a-window-on-the-screen-in-tkinter/
        self.window.update_idletasks()
        
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        
        self.window.mainloop()
        
class MenuBar:

    def __init__(self, window):
        self.menubar = tk.Menu(window)
        window.config(menu=self.menubar)
        
        self.menu_file = MenuFile(self.menubar)
        
        
        self.menu_help = MenuHelp(self.menubar)
        
        
class MenuFile:

    def __init__(self, menubar):
        self.menu_file = tk.Menu(menubar, tearoff=False)
        self.menu_file.add_command(
            label='Exit',
            command=self._on_clicked
        )
        
        menubar.add_cascade(
            label="File",
            menu=self.menu_file
        )
        
    def _on_clicked(self):
        messagebox.showwarning( title="Exit title", message="Exit clicked" )

        
class MenuHelp:

    def __init__(self, menubar):
        self.menu_help = tk.Menu(menubar, tearoff=False)
        self.menu_help.add_command(
            label='About',
            command=self._on_clicked
        )
        
        menubar.add_cascade(
            label="Help",
            menu=self.menu_help
        )
        
    def _on_clicked(self):
        messagebox.showinfo( title="About title", message="About clicked" )
        
    