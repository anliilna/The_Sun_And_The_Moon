import pygame, sys
from button import Button
from level import Level
from settings import *

pygame.init()
screen = pygame.display.set_mode((1200, 600))
pygame.mixer.music.load("When The Sun Loves The Moon.mp3")
pygame.mixer.music.play(-1)
fond = pygame.image.load('game_bg.png')
level = Level(tuto,screen)


def touche():
    """créé un niveau 'tutoriel' pour aider les nouveaux joueurs """
    while True:
        pygame.display.set_caption("Touches")

        screen.blit(fond, (0, 0))
        Z = pygame.image.load('Z.png')
        Q = pygame.image.load('Q.png')
        D = pygame.image.load('D.png')
        haut = pygame.image.load('up.png')
        gauche = pygame.image.load('left.png')
        droite = pygame.image.load('right.png')
        MOUSE_POS = pygame.mouse.get_pos()
        BACK = Button(image=None,
                      pos=(75, 25),
                      text_input="BACK",
                      font=pygame.font.Font("font.ttf", 30),
                      base_color=((215, 252, 212)),
                      hovering_color=((255, 255, 255)))
        FINISH = Button(image=None,
                      pos=((1200/2), 120),
                      text_input="FINISH",
                      font=pygame.font.Font("font.ttf", 65),
                      base_color=((215, 252, 212)),
                      hovering_color=((255, 255, 255)))

        for button in [BACK, FINISH]:
            button.changeColor(MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(MOUSE_POS):
                    from start_window import main_menu
                    main_menu()
                if FINISH.checkForInput(MOUSE_POS):
                    from main import play
                    play()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            droite = pygame.transform.scale(droite, (90, 90))
        if keys[pygame.K_LEFT]:
            gauche = pygame.transform.scale(gauche, (90, 90))
        if keys[pygame.K_UP]:
            haut = pygame.transform.scale(haut, (90, 90))
        if keys[pygame.K_d]:
            D = pygame.transform.scale(D, (90, 90))
        if keys[pygame.K_a]:
            Q = pygame.transform.scale(Q, (90, 90))
        if keys[pygame.K_w]:
            Z = pygame.transform.scale(Z, (90, 90))
        screen.blit(Z, (206, 86))
        screen.blit(Q, (100, 204))
        screen.blit(D, (312, 204))
        screen.blit(haut, (898, 86))
        screen.blit(gauche, (792, 204))
        screen.blit(droite, (1004, 204))

        level.run()
        pygame.display.update()

touche()