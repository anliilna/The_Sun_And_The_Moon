import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Menu")
pygame.mixer.music.load("When The Sun Loves The Moon.mp3")
pygame.mixer.music.play(-1)
BG = pygame.image.load('game_bg.png')
playing = True

def get_font(size):
    return pygame.font.Font("font.ttf", size)

def options():
    """fenêtre options: affiche des bouttons pour les niveaux"""
    while playing:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTIONS_BACK = Button(image=None,
                              pos=(640, 560),
                              text_input="BACK",
                              font=get_font(75),
                              base_color=((215, 252, 212)),
                              hovering_color=((255, 255, 255)))
        LVL_0 = Button(image=None,
                       pos=(150, 50),
                       text_input="LVL 0",
                       font=get_font(50),
                       base_color=((215, 252, 212)),
                       hovering_color=((255, 255, 255)))
        LVL_1 = Button(image=None,
                       pos=(450, 50),
                       text_input="LVL 1",
                       font=get_font(50),
                       base_color=((215, 252, 212)),
                       hovering_color=((255, 255, 255)))
        LVL_2 = Button(image=None,
                       pos=(750, 50),
                       text_input="LVL 2",
                       font=get_font(50),
                       base_color=((215, 252, 212)),
                       hovering_color=((255, 255, 255)))
        LVL_3 = Button(image=None,
                       pos=(1050, 50),
                       text_input="LVL 3",
                       font=get_font(50),
                       base_color=((215, 252, 212)),
                       hovering_color=((255, 255, 255)))

        for button in [OPTIONS_BACK, LVL_0, LVL_1, LVL_2, LVL_3]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        main_menu()
                if LVL_0.checkForInput(OPTIONS_MOUSE_POS):
                    from touches import touche
                    touche()
                for level in [LVL_0, LVL_1, LVL_2, LVL_3]:
                    if level.checkForInput(OPTIONS_MOUSE_POS):
                        from main import play
                        play()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def main_menu():  # création de l'écran d'accueil
    bg = ['bg0.png', 'bg1.png', 'bg2.png', 'bg3.png', 'bg4.png', 'bg5.png', 'bg6.png', 'bg7.png']
    frame_index = 0
    animation_speed = 0.19

    while playing:
        frame_index += animation_speed
        if frame_index >= len(bg):
            frame_index = 0

        BG = pygame.image.load(bg[int(frame_index)])
        pygame.display.set_caption("Menu")
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=None,
                             pos=(600, 300),
                             text_input="PLAY",
                             font=get_font(50),
                             base_color=((215, 252, 212)),
                             hovering_color=((255,255,255)))
        OPTIONS_BUTTON = Button(image=None,
                                pos=(600, 425),
                                text_input="OPTIONS",
                                font=get_font(50),
                                base_color=((215, 252, 212)),
                                hovering_color=((255, 255, 255)))
        QUIT_BUTTON = Button(image=None,
                             pos=(600, 550),
                             text_input="QUIT",
                             font=get_font(50),
                             base_color=((215, 252, 212)),
                             hovering_color=((255, 255, 255)))

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    from touches import touche
                    touche()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        clock.tick(60)
        pygame.display.update()

main_menu()