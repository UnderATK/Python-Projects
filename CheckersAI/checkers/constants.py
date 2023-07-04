import pygame

# Board size
WIDTH, HEIGHT = 800, 800
# Checkers board
ROWS, COLS = 8, 8
# Square size
SQUARE_SIZE = WIDTH//COLS

# RGB Colors
LIGHT_BROWN = (222, 184, 135)
DARKER_BROWN = (139, 69, 19)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GREY = (211, 211, 211)

# King Crown
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (45, 25))