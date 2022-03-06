
# Event manager

import pygame

from gui.guiObjects import snake, food, counter

class eventManager():

    def __init__(self, viewPort: pygame.Surface) -> None:
        self._viewPort = viewPort
        self._snake = snake(250, 250)
        self._score = counter(10, 10)
        self._gameOver = False
        self._clock = pygame.time.Clock()

    def viewPort(self):
        return self._viewPort

    def snake(self):
        return self._snake

    def isGameOver(self) -> bool:
        return self._gameOver

    def gameOver(self) -> None:
        self._gameOver = True

    def checkEvent(self, event) -> None:
        if event.type == pygame.QUIT:
            self.gameOver()

        if event.type == pygame.KEYDOWN:
            self.checkKey(event)

    def checkKey(self, event) -> None:
        if event.key == pygame.K_LEFT:
            self._snake.move(-10, 0)
        
        elif event.key == pygame.K_RIGHT:
            self._snake.move(10, 0)
