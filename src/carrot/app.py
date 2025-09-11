import sys
import shlex

from carrot.view.window import Window
from carrot.model.state import State
from carrot.controller.controller import Controller

class App:

    def __init__(self):
        self._window = Window(shlex.join(sys.argv))
        self._state = State()
        self._controller = Controller(self._window, self._state)
    
    def run(self) -> int:
        self._window.show()
        return 0

if __name__ == '__main__':
    app = App()
    sys.exit(app.run())
