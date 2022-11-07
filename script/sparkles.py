import pygame
class Sparkle_effect(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        self.frame_index = 0
        self.animation_speed = 0.5
        if type == 'jump' or type == 'fall':
            self.frames = [pygame.image.load('sparkles0.png'),
                           pygame.image.load('sparkles1.png'),
                           pygame.image.load('sparkles2.png'),
                           pygame.image.load('sparkles3.png'),
                           pygame.image.load('sparkles4.png'),
                           pygame.image.load('sparkles5.png'),
                           pygame.image.load('sparkles6.png')]
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_Rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.direction.x =0

    def update(self, x_shift):
        self.animate()
        self.rect.x += shift