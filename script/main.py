import pygame, sys
from settings import *
from level import Level
from button import Button


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
fond = pygame.image.load('game_bg.png')
clock = pygame.time.Clock()
pygame.mixer.music.load("When The Sun Loves The Moon.mp3")
pygame.mixer.music.play(-1)
level_map = level_map0
level = Level(level_map, screen)
playing = True

def play():
    """ prend en compte les sprites et positions des joueurs et des 'tiles' et créée l'interface du jeu
        ajoute un boutton BACK pour revenir à l'écran d'accueil"""
    while playing:
        pygame.display.set_caption("When The Sun Loves The Moon")
        screen.blit(fond, (0, 0))
        MOUSE_POS = pygame.mouse.get_pos()
        BACK = Button(image=None,
                      pos=(75, 25),
                      text_input="BACK",
                      font=pygame.font.Font("font.ttf", 30),
                      base_color=((215, 252, 212)),
                      hovering_color=((255, 255, 255)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(MOUSE_POS):
                    from start_window import main_menu
                    main_menu()

        level.run()
        BACK.changeColor(MOUSE_POS)
        BACK.update(screen)
        pygame.display.update()
        clock.tick(60)
play()