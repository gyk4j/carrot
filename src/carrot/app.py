import sys
import shlex

#from model.model import Model
from view.view import Window
from view.view import MenuBar
from view.view import MenuFile
from view.view import MenuHelp
#from controller.controller import Controller

class App:

    def __init__(self):
        self.window = Window(shlex.join(sys.argv))
    
    def run(self) -> int:
        self.window.show()
        return 0

if __name__ == '__main__':
    app = App()
    sys.exit(app.run())
