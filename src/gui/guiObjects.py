
# Here are the main objects in GUI


from typing import List


class _guiObject():

    def __init__(self, name: str, x: int, y: int) -> None:
        self._name = name
        self._x = x
        self._y = y

    def getName(self) -> str:
        return self._name

    def getPosition(self) -> List:
        return [self._x, self._y]

    def changePosition(self, newX: int, newY: int) -> None:
        self._x = newX
        self._y = newY

    def move(self, addX: int, addY: int) -> None:
        self._x += addX
        self._y += addY


class food(_guiObject):

    def __init__(self, x: int, y: int) -> None:
        super().__init__("Food", x, y)


class snake(_guiObject):

    def __init__(self, x: int, y: int) -> None:
        super().__init__("Snake", x, y)
        self._length = 1
        self._size = 10
    
    def size(self) -> int:
        return self._size


class counter(_guiObject):

    def __init__(self, x: int, y: int) -> None:
        super().__init__("Counter", x, y)
        self._counter = 0

    def addPoint(self) -> int:
        self._counter += 1
        return self._counter

    def resetCounter(self) -> int:
        self._counter = 0
        return self._counter
