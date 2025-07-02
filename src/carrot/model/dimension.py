class Dimension:

    # In Python, dimension is usually expressed as a 2-tuple,
    # but we explicitly use 2 int fields/properties for it here.

    def __init__(self, width:int = 0, height:int = 0):
        self._width: int = width
        self._height: int = height

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height):
        self._height = height
