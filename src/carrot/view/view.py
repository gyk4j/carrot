import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage

class Window:

    def __init__(self, title):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry("%dx%d" % (1024, 640))
        
        # Add menu bar
        self.menubar = MenuBar(self.window)
        
        # Add tool bar
        self.toolbar = ToolBar(self.window)
    
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

# Source: https://pythonexamples.org/python-tkinter-label-tooltip/        
class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show)
        self.widget.bind("<Leave>", self.hide)

    def show(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 32
        y += self.widget.winfo_rooty() + 32

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = ttk.Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1, padding=(6,1,6,1))
        label.pack()

    def hide(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None
