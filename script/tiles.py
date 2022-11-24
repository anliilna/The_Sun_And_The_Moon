import pygame, random

class Tile(pygame.sprite.Sprite):
    """ créée les 'tiles' en prenant en compte leur image et leur taille"""
    def __init__(self, pos, size):
        super().__init__()
        nbr = random.randint(0, 1)
        self.image = pygame.image.load(f"tiles{nbr}.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift

class Win(pygame.sprite.Sprite):
    """prend en compte la taille de l'image et créée une 'tile'"""
    def __init__(self, pos, size):
        super().__init__()
        nbr = random.randint(0, 1)
        self.image = pygame.image.load(f"finish_platform{nbr}.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift