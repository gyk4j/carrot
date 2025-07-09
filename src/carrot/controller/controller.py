
class Controller:

    def __init__(self, view, model):
        self._view = view
        self._model = model

        # Menu
        if self.file_new is None:
            print("self.file_new is None!")

        self.view.menubar.menu_file_new.onclick = self.file_new
        self.view.menubar.menu_file_open.onclick = self.file_open
        self.view.menubar.menu_file_save.onclick = self.file_save
        self.view.menubar.menu_file_saveas.onclick = self.file_saveas
        self.view.menubar.menu_file_exit.onclick = self.file_exit

        self.view.menubar.menu_go_back.onclick = self.go_back
        self.view.menubar.menu_go_next.onclick = self.go_forward

        self.view.menubar.menu_help_about.onclick = self.help_about
        
        # Tool Bar
        self.view.toolbar.file_new.onclick = self.file_new
        self.view.toolbar.file_open.onclick = self.file_open
        self.view.toolbar.file_save.onclick = self.file_save
        self.view.toolbar.file_saveas.onclick = self.file_saveas
        self.view.toolbar.file_exit.onclick = self.file_exit

        self.view.toolbar.go_back.onclick = self.go_back
        self.view.toolbar.go_forward.onclick = self.go_forward

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

    def file_exit(self):
        self._view.notify("Exit", "File > Exit")

    def go_back(self):
        self._view.notify("Back", "Go > Back")

    def go_forward(self):
        self._view.notify("Forward", "Go > Forward")

    def help_about(self):
        self._view.notify("About", "Help > About")


