from model.point import Point
from model.dimension import Dimension

class Selection:

    def __init__(self, point = Point(), dimension = Dimension()):
        self._point: Point = point
        self._dimension: Dimension = dimension

    @property
    def point(self) -> Point:
        return self._point

    @point.setter
    def point(self, point: Point):
        self._point = point

    @property
    def dimension(self) -> Dimension:
        return self._dimension

    @dimension.setter
    def dimension(self, dimension: Dimension):
        self._dimension = dimension
