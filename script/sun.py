import pygame

class Sun(pygame.sprite.Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        # sparkles
        self.display_surface = surface
        self.sparkles_img()
        self.sparkles_frame_index = 0
        self.sparkles_animation_speed = 0.5

        # player animations
        self.frame_index = 0
        self.animation_speed = 0.15
        self.animations = {'idle': [pygame.image.load('Sun_idle0.png'),
                                    pygame.image.load('Sun_idle1.png'),
                                    pygame.image.load('Sun_idle2.png'),
                                    pygame.image.load('Sun_idle3.png')],
                           'walk': [pygame.image.load('Sun_walk0.png'),
                                    pygame.image.load('Sun_walk1.png'),
                                    pygame.image.load('Sun_walk2.png'),
                                    pygame.image.load('Sun_walk3.png'),
                                    pygame.image.load('Sun_walk4.png'),
                                    pygame.image.load('Sun_walk5.png')],
                           'jump': [pygame.image.load('Sun_fall0.png')],
                           'fall': [pygame.image.load('Sun_fall0.png')]}
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.status = 'idle'

        # player movement
        self.sens = '0'
        self.saut = False
        self.fall = False
        self.speed = 10
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 1.5
        self.jump_speed = -16

    def sparkles_img(self):
        self.sparkles = [pygame.image.load('sparkles_walk0.png'),
                         pygame.image.load('sparkles_walk1.png'),
                         pygame.image.load('sparkles_walk2.png'),
                         pygame.image.load('sparkles_walk3.png'),
                         pygame.image.load('sparkles_walk4.png'),
                         pygame.image.load('sparkles_walk5.png'),
                         pygame.image.load('sparkles_walk6.png')]

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.sens = 'droite'
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.sens = 'gauche'
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pygame.K_w]:
            if not self.saut:
                self.jump()

    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.sens == 'droite':
            self.image = image
        else:
            flipped = pygame.transform.flip(image, True, False)
            self.image = flipped

    def sparkles_animation(self):
        if self.status == 'walk':
            self.sparkles_frame_index += self.sparkles_animation_speed
            if self.sparkles_frame_index >= len(self.sparkles):
                self.sparkles_frame_index = 0

            sparkles = self.sparkles[int(self.sparkles_frame_index)]

            if self.sens == 'droite':
                pos = self.rect.bottomleft - pygame.math.Vector2(20, 24)
                self.display_surface.blit(sparkles, pos)
            if self.sens == 'gauche':
                pos = self.rect.bottomright - pygame.math.Vector2(12, 24)
                flipped = pygame.transform.flip(sparkles, True, False)
                sparkles = flipped
                self.display_surface.blit(sparkles, pos)

    def get_status(self):
        if self.direction.y > 1:
            self.status = 'fall'
        elif self.direction.y < 0:
            self.status = 'jump'
        else:
            if self.direction.x != 0:
                self.animation_speed = 0.5
                self.status = 'walk'
            else:
                self.animation_speed = 0.15
                self.status = 'idle'
            self.saut = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.saut = True
        self.direction.y = self.jump_speed

    def update(self):
        self.get_status()
        self.get_input()
        self.animate()
        self.sparkles_animation()