import tkinter as tk

from .statusbarpane import StatusBarPane

class StatusBar:

    def __init__(self, window):
        self._statusbar = tk.Frame(window)
        
        self._statusbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        self._statusbar_file = StatusBarPane(self._statusbar, True)
        self._statusbar_progress = StatusBarPane(self._statusbar, False)
        self._statusbar_mouse = StatusBarPane(self._statusbar, False)
        self._statusbar_selection = StatusBarPane(self._statusbar, False)
        
        self.statusbar_file.set_text('C:\Windows')
        self.statusbar_progress.set_text('1 / 999')
        self.statusbar_mouse.set_text("%d, %d" % (123, 456))
        self.statusbar_selection.set_text("%d x %d pixels" % (300, 600))

    @property
    def statusbar(self) -> tk.Frame:
        return self._statusbar

    @property
    def statusbar_file(self) -> StatusBarPane:
        return self._statusbar_file

    @property
    def statusbar_progress(self) -> StatusBarPane:
        return self._statusbar_progress

    @property
    def statusbar_mouse(self) -> StatusBarPane:
        return self._statusbar_mouse

    @property
    def statusbar_selection(self) -> StatusBarPane:
        return self._statusbar_selection