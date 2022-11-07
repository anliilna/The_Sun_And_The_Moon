import pygame, sys
from settings import *
from level import Level
from button import Button

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
fond = pygame.image.load('game_bg.png')
clock = pygame.time.Clock()
pygame.display.set_caption("When The Sun Loves The Moon")
pygame.mixer.music.load("When The Sun Loves The Moon.mp3")
pygame.mixer.music.play(-1)
level_map = level_map0
level = Level(level_map,screen)

while True:
    screen.blit(fond, (0, 0))
    MOUSE_POS = pygame.mouse.get_pos()
    BACK = Button(image=None, pos=(75, 25),
                          text_input="BACK", font=pygame.font.Font("font.ttf", 30),
                          base_color=((215, 252, 212)),
                          hovering_color=((255, 255, 255)))
    BACK.changeColor(MOUSE_POS)
    BACK.update(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if BACK.checkForInput(MOUSE_POS):
                from start_window import *
                main_menu()
                import main_menu

    level.run()

    pygame.display.update()
    clock.tick(60)