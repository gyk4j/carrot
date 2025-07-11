
class Controller:

    def __init__(self, view, model):
        self._view = view
        self._model = model

        # Menu
        self.view.menubar.menu_file_new.onclick = self.file_new
        self.view.menubar.menu_file_open.onclick = self.file_open
        self.view.menubar.menu_file_save.onclick = self.file_save
        self.view.menubar.menu_file_saveas.onclick = self.file_saveas
        self.view.menubar.menu_file_export.onclick = self.file_export
        self.view.menubar.menu_file_exit.onclick = self.file_exit

        self.view.menubar.menu_go_back.onclick = self.go_back
        self.view.menubar.menu_go_next.onclick = self.go_forward

        self.view.menubar.menu_selection_contract.onclick = self.selection_contract
        self.view.menubar.menu_selection_expand.onclick = self.selection_expand
        self.view.menubar.menu_selection_mark.onclick = self.selection_mark

        self.view.menubar.menu_help_view.onclick = self.help_view
        self.view.menubar.menu_help_about.onclick = self.help_about

        # Hacks for menu accelerator
        self.view.add_accelerator('<Control-n>', self.file_new) 
        self.view.add_accelerator('<Control-o>', self.file_open)
        self.view.add_accelerator('<Control-s>', self.file_save)
        self.view.add_accelerator('<Control-S>', self.file_saveas)
        self.view.add_accelerator('<Control-Alt-e>', self.file_export)
        self.view.add_accelerator('<Control-x>', self.file_exit)
        self.view.add_accelerator('<Alt-Left>', self.go_back)
        self.view.add_accelerator('<Alt-Right>', self.go_forward)
        self.view.add_accelerator('<Control-minus>', self.selection_contract)
        self.view.add_accelerator('<Control-plus>', self.selection_expand)
        self.view.add_accelerator('<Return>', self.selection_mark)
        self.view.add_accelerator('<F1>', self.help_view)
        
        # Tool Bar
        self.view.toolbar.file_new.onclick = self.file_new
        self.view.toolbar.file_open.onclick = self.file_open
        self.view.toolbar.file_save.onclick = self.file_save
        self.view.toolbar.file_saveas.onclick = self.file_saveas
        self.view.toolbar.file_export.onclick = self.file_export
        self.view.toolbar.file_exit.onclick = self.file_exit

        self.view.toolbar.go_back.onclick = self.go_back
        self.view.toolbar.go_forward.onclick = self.go_forward

        self.view.toolbar.selection_contract.onclick = self.selection_contract
        self.view.toolbar.selection_expand.onclick = self.selection_expand
        self.view.toolbar.selection_mark.onclick = self.selection_mark

        # Set sample text
        self.view.title = 'Hello World' 
        self.view.statusbar.statusbar_file.text = 'C:\TEMP'
        self.view.statusbar.statusbar_progress.text = '123 / 987'
        self.view.statusbar.statusbar_mouse.text = "%d, %d" % (666, 999)
        self.view.statusbar.statusbar_selection.text = "%d x %d pixels" % (100, 200)

    @property
    def view(self):
        return self._view

    @property
    def model(self):
        return self._model

    def file_new(self):
        self._view.notify("New", "File > New")

    def file_open(self):
        self._view.notify("Open", "File > Open")

    def file_save(self):
        self._view.notify("Save", "File > Save")

    def file_saveas(self):
        self._view.notify("Save As", "File > Save As")

    def file_export(self):
        self._view.notify("Export", "File > Export")

    def file_exit(self):
        self._view.notify("Exit", "File > Exit")
        self._view.window.destroy()

    def go_back(self):
        self._view.notify("Back", "Go > Back")

    def go_forward(self):
        self._view.notify("Forward", "Go > Forward")

    def selection_contract(self):
        self._view.notify("Contract", "Selection > Contract")

    def selection_expand(self):
        self._view.notify("Expand", "Selection > Expand")

    def selection_mark(self):
        self._view.notify("Mark", "Selection > Mark")

    def help_view(self):
        self._view.notify("View Help", "Help > View Help")

    def help_about(self):
        self._view.notify("About Carrot", "Help > About Carrot")


