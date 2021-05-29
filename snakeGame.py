import random
import pygame
import sys
from pygame.locals import *
from settingsSnakeFun import *


def main():
    global CLOCK, SCREEN, FONT

    pygame.init()
    CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((Width_window, height_window))
    pygame.display.set_caption('Snake Game')
    showStartScreen()
    while True:

        runGame()

        showGameOverScreen()


def runGame():
    startx = random.randint(5, cell_width - 6)
    starty = random.randint(5, cell_height - 6)
    global worm

    worm = [{'x': startx, 'y': starty}, {'x': startx -
                                         1, 'y': starty}, {'x': startx-2, 'y': starty}]

    direction = UP

    food = getRandomLocation()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        if worm[HEAD]['x'] == -1 or worm[HEAD]['x'] == cell_width or worm[HEAD]['y'] == -1 or worm[HEAD]['y'] == cell_height:
            return
        for wormBody in worm[1:]:
            if wormBody['x'] == worm[HEAD]['x'] and wormBody['y'] == worm[HEAD]['y']:
                return
        if worm[HEAD]['x'] == food['x'] and worm[HEAD]['y'] == food['y']:
            food = getRandomLocation()
        else:
            del worm[-1]

        if direction == UP:
            newHead = {'x': worm[HEAD]['x'], 'y': worm[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': worm[HEAD]['x'], 'y': worm[HEAD]['y'] + 1}
        elif direction == RIGHT:
            newHead = {'x': worm[HEAD]['x'] + 1, 'y': worm[HEAD]['y']}
        elif direction == LEFT:
            newHead = {'x': worm[HEAD]['x'] - 1, 'y': worm[HEAD]['y']}
        worm.insert(0, newHead)

        SCREEN.FILL(BGCOLOR)
        drawGrid()
        drawWorm(worm)
        drawfood(food)
        drawScore((len(worm) - 3) * 10)
        pygame.display.update()
        CLOCK.tick(FPS)
