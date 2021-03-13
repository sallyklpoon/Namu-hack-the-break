"""
Member List
- Batchansaa Batzorig
- Dmitri Golota
- Sally Poon
- Subin Moon
- Martin Gatchev

Mar 13, 2021
"""

import pygame
import sys
import random
from pygame_functions import *


pygame.init()
pygame.display.set_caption("Namu")

WINDOW_SIZE = (500, 500)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
clock = pygame.time.Clock()

# Game Variables
testSprite = newSprite("./assets/Namu1.gif", 12) # 12 is the gif frame
game_font = pygame.font.Font('./assets/Fipps_font.otf', 7)
score = 0
high_score = 100

# Floor_Sand
sand = pygame.image.load('./assets/sand.png').convert()
sand = pygame.transform.scale(sand, (512, 512))


# Game Functions
def movement():
    nextFrame = clock()
    frame = 0
    while True:
        if clock() > nextFrame:
            frame = (frame + 1) % 12
            nextFrame += 120
        if keyPressed("right"):
            changeSpriteImage(testSprite, 0*12 + frame)
        elif keyPressed("down"):
            changeSpriteImage(testSprite, 1*12 + frame)
        elif keyPressed("left"):
            changeSpriteImage(testSprite, 2*12 + frame)
        elif keyPressed("right"):
            changeSpriteImage(testSprite, 3*12 + frame)


def score_display():
    score_surface = game_font.render(str(score), True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(250, 25))
    screen.blit(score_surface, score_rect)


# Main Loop
game_active = True
game_running = True

while game_running:
    pygame.time.delay(100)
    for event in pygame.event.get():      # catch all the events that are happening right now
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game_active:

        # Game Functions
        # image of player
        # background image
        score_display()

    screen.blit(sand, (0, 0))

    pygame.display.update()
    clock.tick(120)