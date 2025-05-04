import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg1 = pygame.image.load('cat.png')
cat1x = 10
cat1y = 10
direction1 = 'right'

catImg2 = pygame.image.load('cat.png')
cat2x = 280
cat2y = 220
direction2 = 'left'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction1 == 'right':
        cat1x += 5
        if cat1x == 280:
            direction1 = 'down'
    elif direction1 == 'down':
        cat1y += 5
        if cat1y == 220:
            direction1 = 'left'
    elif direction1 == 'left':
        cat1x -= 5
        if cat1x == 10:
            direction1 = 'up'
    elif direction1 == 'up':
        cat1y -= 5
        if cat1y == 10:
            direction1 = 'right'

    if direction2 == 'right':
        if cat2x == 10:
            direction2 = 'up'
        cat2x -= 5
    elif direction2 == 'down':
        if cat2y == 10:
            direction2 = 'right'
        cat2y -= 5
    elif direction2 == 'left':
        if cat2x == 280:
            direction2 = 'down'
        cat2x += 5
    elif direction2 == 'up':
        if cat2y == 220:
            direction2 = 'left'
        cat2y += 5

    DISPLAYSURF.blit(catImg1, (cat1x, cat1y))
    DISPLAYSURF.blit(catImg2, (cat2x, cat2y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
