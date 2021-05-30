import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.font.init()

FPS = 3
Width_window = 720
height_window = 600
size_cell = 30
assert height_window % size_cell == 0, "Window Height must be a multiple of Cell Size"
assert Width_window % size_cell == 0, "Window Width must be a multiple of Cell Size"
cell_width = int(Width_window / size_cell)
cell_height = int(height_window / size_cell)

WHITE = (255, 255, 255)
BLACK = (0,     0,   0)
GREEN = (0,   255,   0)

RED = (255,   0,   0)

DARKGREEN = (0,   155,   0)
DARKGRAY = (40,   40,  40)
YELLOW = (255, 255,   0)

BGCOLOR = WHITE

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0
