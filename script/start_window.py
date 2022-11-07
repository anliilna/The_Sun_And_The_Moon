import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Menu")
pygame.mixer.music.load("When The Sun Loves The Moon.mp3")
pygame.mixer.music.play(-1)
BG = pygame.image.load("game_bg.png")

def get_font(size):
    return pygame.font.Font("font.ttf", size)

def play():  # fenêtre du niveau
    while True:
        import main

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def options():  # fenêtre options
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color=((215, 252, 212)), hovering_color=((255,255,255)))
        LVL_0 = Button(image=None, pos=(200, 50),
                            text_input="LVL 0", font=get_font(75), base_color=((215, 252, 212)), hovering_color=((255,255,255)))

        for button in [OPTIONS_BACK, LVL_0]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if LVL_0.checkForInput(OPTIONS_MOUSE_POS):
                    import main
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def main_menu():  # création de l'écran d'accueil
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("When The Sun", True, ((255, 211, 140)))
        MENU_TEXT0 = get_font(50).render("Loves The Moon", True, ((195, 221, 231)))
        MENU_RECT = MENU_TEXT.get_rect(center=(600, 60))
        MENU_RECT0 = MENU_TEXT0.get_rect(center=(600, 140))

        PLAY_BUTTON = Button(image=None, pos=(600, 250),
                             text_input="PLAY", font=get_font(50),base_color=((215, 252, 212)), hovering_color=((255,255,255)))
        OPTIONS_BUTTON = Button(image=None, pos=(600, 375),
                                text_input="OPTIONS", font=get_font(50), base_color=((215, 252, 212)), hovering_color=((255,255,255)))
        QUIT_BUTTON = Button(image=None, pos=(600, 500),
                             text_input="QUIT", font=get_font(50), base_color=((215, 252, 212)), hovering_color=((255,255,255)))

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(MENU_TEXT0, MENU_RECT0)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()