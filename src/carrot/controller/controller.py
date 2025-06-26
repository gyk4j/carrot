from controller.event import ActionEvent
from model.model import Model

class Controller:

    def __init__(self, view, model: Model):
        self._view = view
        self._model = model

    def go_back(self, action_event: ActionEvent):
        self._model.current -= 1
        print("%s: %s" % (action_event.action_command, action_event.source))

    def go_forward(self, action_event: ActionEvent):
        self._model.current += 1
        print("%s: %s" % (action_event.action_command, action_event.source))