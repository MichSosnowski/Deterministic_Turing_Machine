class WindowSize:

    def __init__(self, width: int, height: int) -> None:
        self._width: int = width
        self._height: int = height

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height
