from .point import Point
from .aspect_ratio import AspectRatio
from .dimension import Dimension

class Selection:

    def __init__(self, 
        crc32 = 0,
        file_size = 0,
        image_size = Dimension(),
        point = Point(), 
        factor = 1.0):
        
        self._crc32: int = crc32
        self._file_size: int = file_size
        self._image_size: Dimension = image_size
        
        self._point: Point = point
        self._factor: float = factor
        
    @property
    def id(self) -> str:
        return str.format('{:08x}{:08x}', self._crc32, self._file_size)
        # return format(self._crc32, '08x') + format(self._file_size, '08x')
        
    @property
    def crc32(self) -> int:
        return self._crc32

    @crc32.setter
    def crc32(self, crc32: int):
        self._crc32 = crc32
        
    @property
    def file_size(self) -> int:
        return self._file_size
        
    @file_size.setter
    def file_size(self, file_size: int):
        self._file_size = file_size
        
    @property
    def image_size(self) -> Dimension:
        return self._image_size

    @image_size.setter
    def image_size(self, image_size: Dimension):
        self._image_size = image_size
    
    @property
    def point(self) -> Point:
        return self._point

    @point.setter
    def point(self, point: Point):
        self._point = point
        
    @property
    def factor(self) -> float:
        return self._factor

    @factor.setter
    def factor(self, factor: float):
        self._factor = factor
        
    def get_dimension(self, aspect_ratio: AspectRatio) -> Dimension:
        width = self.image_size.width * self.factor * aspect_ratio.horizontal
        height = self.image_size.height * self.factor * aspect_ratio.vertical
        return Dimension(width = width, height = height)
