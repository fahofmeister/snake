
# Here are the main objects in GUI

from typing import Coroutine, Tuple


class _guiObject():

    def __init__(self, name: str, coord: Tuple[int, int]) -> None:
        self._name = name
        self._coord = coord

    def getName(self) -> str:
        return self._name

    def getPosition(self) -> Tuple[int, int]:
        return self._coord

    def changePosition(self, newCoord: Tuple[int, int]) -> None:
        self._coord = newCoord


class food(_guiObject):

    def __init__(self, coord: Tuple[int, int]) -> None:
        super().__init__("Food", coord)


class snake(_guiObject):

    def __init__(self, coord: Tuple[int, int]) -> None:
        super().__init__("Snake", coord)
        self._length = 1


class counter(_guiObject):

    def __init__(self, coord: Tuple[int, int]) -> None:
        super().__init__("Counter", coord)
        self._counter = 0

    def addPoint(self) -> int:
        self._counter += 1
        return self._counter

    def resetCounter(self) -> int:
        self._counter = 0
        return self._counter
