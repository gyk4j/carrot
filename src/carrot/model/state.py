from model.selection import Selection

class State:

    def __init__(self):

        self._db: str = ''
        self._image: str = ''

        self._processed: int = 0
        self._total: int = 0

        # Factor is expressed as a percentage of the image size.
        # E.g. 10%, 20%, 30% ... 100%
        # At the moment, the delta is fixed at +-10% i.e. 0.1.
        # The selection dimension is calculated from factor x image size, 
        # and constrained by the chosen aspect ratio.
        self._factor: float = 0.0
        self._selection: Selection = Selection(p, d)

    @property
    def db(self) -> str:
        return self._db

    @db.setter
    def db(self, db: str):
        self._db = db

    @property
    def image(self) -> str:
        return self._image

    @image.setter
    def image(self, image: str):
        self._image = image

    @property
    def processed(self) -> int:
        return self._processed

    @processed.setter
    def processed(self, processed: int):
        self._processed = processed

    @property
    def total(self) -> int:
        return self._total

    @total.setter
    def total(self, total: int):
        self._total = total

    @property
    def factor(self) -> float:
        return self._factor

    @factor.setter
    def factor(self, factor: float):
        self._factor = factor

    @property
    def selection(self) -> Selection:
        return self._selection

    @selection.setter
    def selection(self, selection: Selection):
        self._selection = selection
