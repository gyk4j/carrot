class AspectRatio:

    def __init__(self, horizontal:int = 1, vertical:int = 1):
        self._horizontal: int = horizontal
        self._vertical: int = vertical

    @property
    def horizontal(self) -> int:
        return self._horizontal

    @horizontal.setter
    def horizontal(self, horizontal):
        self._horizontal = horizontal

    @property
    def vertical(self) -> int:
        return self._vertical

    @vertical.setter
    def vertical(self, vertical):
        self._vertical = vertical
