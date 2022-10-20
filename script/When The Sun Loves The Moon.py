import pygame
import moon_script
import sys
pygame.init()

value = 0
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("When The Sun Loves The Moon")
fond = pygame.image.load('game_bg-1.png')
moon = moon_script.Moon()
temps = pygame.time.Clock()
time = 15
pygame.mixer.music.load("When The Sun Loves The Moon.mp3")
pygame.mixer.music.play(-1)

running = True

while running:

    screen.blit(fond, (0, 0))
    temps.tick(time)

    if value >= len(moon.anim):
        value = 0
    frame = moon.anim[value]

    for event in pygame.event.get():
        # v si l'événement est le clic sur la fermeture de la fenêtre
        if event.type == pygame.QUIT:
            running = False  # running est sur False
            sys.exit()

    # gestion du clavier
        # v si une touche a été tapée KEYUP quand on relache la touche
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # si la touche est la fleche gauche
                # v on déplace le vaisseau de 1 pixel sur la gauche
                moon.anim = moon.walk_left
                moon.sens = "gauche"
            # v si la touche est la fleche droite
            if event.key == pygame.K_RIGHT:
                # v on déplace le vaisseau de 1 pixel sur la gauche
                moon.anim = moon.walk_right
                moon.sens = "droite"
            if event.key == pygame.K_SPACE:
                moon.saut = True
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            time = 15
        else:
            if moon.sens == "gauche":
                moon.anim = moon.idle
            if moon.sens == "droite":
                moon.anim = moon.idle_right
            moon.sens = '0'
            time = 5

    moon.gravite()
    moon.sauter()
    moon.deplacer()
    screen.blit(frame, [moon.position, moon.hauteur])
    value += 1

    pygame.display.update()