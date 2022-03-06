
import pygame

from gui import displaySize, colors
from gui import eventManager


def main() -> None:
    
    pygame.init()

    viewPort = pygame.display.set_mode(displaySize)
    manager = eventManager.eventManager(viewPort)
    viewPort.fill(colors.black)
    pygame.display.update()
    pygame.display.set_caption("Just Another Snake Game")

    while not manager.isGameOver():
        for event in pygame.event.get():
            manager.checkEvent(event)


if __name__ == "__main__":
    main()
    pygame.quit()
    quit()
