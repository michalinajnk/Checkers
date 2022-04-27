import pygame
WIDTH, HEIGHT = 800, 800
ROW, COLS = 8, 8
FIELD_SIZE = WIDTH // COLS


#color
RED = (255, 0, 0)
GREY = (105,105, 105)
WHITE = (255, 255, 255)

BLUE = (0, 191, 255)
BORD = (165, 42, 42)
BLACK = (0, 0, 0)

#img
KING = pygame.transform.scale(pygame.image.load('assets/crown.png'), (54,35))