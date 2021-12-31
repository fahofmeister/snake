
from typing import List
import pygame
from gui import window_width, window_height, red
from gui import eventManager


def main() -> None:
    
    pygame.init()

    viewPort = pygame.display.set_mode((window_width, window_height))
    manager = eventManager(viewPort)
    pygame.display.update()
    pygame.display.set_caption("Just Another Snake Game")

    while not manager.isGameOver():
        for event in pygame.event.get():
            manager.checkEvent(event)


if __name__ == "__main__":
    main()
    pygame.quit()
    quit()
