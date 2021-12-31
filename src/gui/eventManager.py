
# Event manager

import pygame
from pygame import Surface
from gui.guiObjects import snake, food, counter

class eventManager():

    def __init__(self, dis: Surface) -> None:
        self._snake = snake((250, 250))
        self._score = counter((10, 10))
        self._gameOver = False

    def isGameOver(self) -> bool:
        return self._gameOver

    def gameOver(self) -> None:
        self._gameOver = True

    def checkEvent(self, event) -> None:
        if event.type == pygame.QUIT:
            self.gameOver()
