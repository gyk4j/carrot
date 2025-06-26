class Model:

    def __init(self):
        self._images = [
            "1.jpg",
            "2.jpg",
            "3.jpg",
            "4.jpg",
            "5.jpg",
            "6.jpg",
            "7.jpg",
            "8.jpg",
        ]
        self._current = 0

    @property
    def current(self) -> int:
        return self._current

    @current.setter
    def current(self, current):
        if current < 0:
            self._current = 0
        elif current >= len(self._images):
            self._current = len(self._images) - 1
        else:
            self._current = current

