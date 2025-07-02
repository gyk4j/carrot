class Point:
   
    def __init__(self, x:int = 0, y:int = 0):
        self._x: int = x
        self._y: int = y

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
