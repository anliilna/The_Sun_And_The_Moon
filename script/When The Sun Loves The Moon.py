import pygame, sys
from settings import *
from level import Level

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
fond = pygame.image.load('game_bg.png')
clock = pygame.time.Clock()
level = Level(level_map,screen)
# pygame.mixer.music.load("When The Sun Loves The Moon.mp3")
# pygame.mixer.music.play(-1)

while True:

    screen.blit(fond, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    level.run()

    pygame.display.update()
    clock.tick(60)