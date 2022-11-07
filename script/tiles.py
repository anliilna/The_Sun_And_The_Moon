import pygame, random

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        nbr = random.randint(0, 1)
        self.image = pygame.image.load(f"tiles{nbr}.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift