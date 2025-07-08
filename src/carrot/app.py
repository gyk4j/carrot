import sys
import shlex

from view.window import Window
from model.state import State
#from controller.controller import Controller

class App:

    def __init__(self):
        self._window = Window(shlex.join(sys.argv))
        self._state = State(self._window.window)
    
    def run(self) -> int:
        self._window.show()
        return 0

if __name__ == '__main__':
    app = App()
    sys.exit(app.run())
