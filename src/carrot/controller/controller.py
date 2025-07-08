from controller.event import ActionEvent

class Controller:

    def __init__(self, view, model):
        self._view = view
        self._model = model

    @property
    def view(self):
        return self._view

    @property
    def model(self):
        return self._model

    """
    def go_back(self, action_event: ActionEvent):
        self._model.current -= 1
        print("%s: %s" % (action_event.action_command, action_event.source))

    def go_forward(self, action_event: ActionEvent):
        self._model.current += 1
        print("%s: %s" % (action_event.action_command, action_event.source))
    """