import tkinter as tk

from .toolbarbutton import ToolBarButton
from .toolbarseparator import ToolBarSeparator

class ToolBar:

    def __init__(self, window):
        self._toolbar = tk.Frame(window)
        #(borderwidth = 2, relief=tk.RAISED)
        self._toolbar.pack(side=tk.TOP, fill=tk.X)
        
        self._file_new = ToolBarButton(self._toolbar, "New (Ctrl+N)", "res/ico/file_new.png")
        self._file_open = ToolBarButton(self._toolbar, "Open (Ctrl+O)", "res/ico/file_open.png")
        self._file_save = ToolBarButton(self._toolbar, "Save (Ctrl+S)", "res/ico/file_save.png")
        self._file_saveas = ToolBarButton(self._toolbar, "Save as (Ctrl+Shift+S)", "res/ico/file_saveas.png")
        self._file_export = ToolBarButton(self._toolbar, "Export (Ctrl+Alt+E)", "res/ico/file_export.png")
        self._file_exit = ToolBarButton(self._toolbar, "Exit", "res/ico/file_exit.png")
        self._separator1 = ToolBarSeparator(self._toolbar)
        self._go_back = ToolBarButton(self._toolbar, "Go Back (Alt+Left)", "res/ico/go_back.png")
        self._go_forward = ToolBarButton(self._toolbar, "Go Forward (Alt+Right)", "res/ico/go_forward.png")
        self._separator2 = ToolBarSeparator(self._toolbar)
        self._selection_contract = ToolBarButton(self._toolbar, "Contract (Ctrl+-)", "res/ico/selection_contract.png")
        self._selection_expand = ToolBarButton(self._toolbar, "Expand (Ctrl++)", "res/ico/selection_expand.png")
        self._selection_mark = ToolBarButton(self._toolbar, "Mark (Enter)", "res/ico/selection_mark.png")

    @property
    def toolbar(self) -> tk.Frame:
        return self._toolbar

    @property
    def file_new(self) -> ToolBarButton:
        return self._file_new

    @property
    def file_open(self) -> ToolBarButton:
        return self._file_open

    @property
    def file_save(self) -> ToolBarButton:
        return self._file_save

    @property
    def file_saveas(self) -> ToolBarButton:
        return self._file_saveas

    @property
    def file_export(self) -> ToolBarButton:
        return self._file_export

    @property
    def file_exit(self) -> ToolBarButton:
        return self._file_exit

    @property
    def go_back(self) -> ToolBarButton:
        return self._go_back

    @property
    def go_forward(self) -> ToolBarButton:
        return self._go_forward

    @property
    def selection_contract(self) -> ToolBarButton:
        return self._selection_contract

    @property
    def selection_expand(self) -> ToolBarButton:
        return self._selection_expand

    @property
    def selection_mark(self) -> ToolBarButton:
        return self._selection_mark
