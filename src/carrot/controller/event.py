import time

class ActionEvent:
    ACTION_FIRST = 1001
    ACTION_LAST = 1001
    ACTION_PERFORMED = 1001
    ALT_MASK = 8
    CTRL_MASK = 2
    META_MASK = 4
    SHIFT_MASK = 1

    def __init__(self, source, id, command, when=0, modifiers=0):
        self._source = source
        self._id = id
        self._action_command = command
        
        if when == 0:
            self._when = time.time()
        else:
            self._when = when

        self._modifiers = modifiers

    @property
    def action_command(self) -> str:
        return self._action_command
    
    @property
    def modifiers(self) -> int:
        return self._modifiers

    @property
    def when(self) -> int:
        return self._when

""" 
"""
class ActionListener:
    def actionPerformed(self, e: ActionEvent):
        pass