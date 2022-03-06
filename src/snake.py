
import pygame

from gui import displaySize, colors, __title__, __version__, drawBoard
from gui import eventManager


def main() -> None:
    
    pygame.init()

    viewPort = pygame.display.set_mode(displaySize)
    manager = eventManager.eventManager(viewPort)
    drawBoard(manager)
    pygame.display.set_caption(f'{__title__} - {__version__}')

    while not manager.isGameOver():
        for event in pygame.event.get():
            manager.checkEvent(event)


if __name__ == "__main__":
    main()
    pygame.quit()
    quit()
