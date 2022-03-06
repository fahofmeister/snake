
# Module to provide general configuration for GUI

__version__ = "alpha"
__title__ = "Just Another Snake Game"

# Default specs
window_width = 500
window_height = 500
displaySize = (window_width, window_height)

# Default defs
import pygame
from gui import colors

def drawBoard(manager: object):
    
    viewPort = manager.viewPort()
    snake = manager.snake()

    viewPort.fill(colors.black)
    pygame.draw.rect(
        viewPort,
        colors.blue,
        [
            snake.getPosition()[0],
            snake.getPosition()[1],
            snake.size(),
            snake.size()
        ]
    )
    pygame.display.update()

