import pygame

class Player(pygame.sprite.Sprite):
    """classe qui créé le premier personnage 'Sun', qui prend en compte ses images,
    sa vitesse de déplacements, sa gravité et les touches qui définissent ses mouvements"""
    def __init__(self, pos):
        super().__init__()
        # images, vitesse par image
        self.frame_index = 0
        self.animation_speed = 0.15
        self.animations = {'idle': [pygame.image.load('Moon_idle0.png'),
                                    pygame.image.load('Moon_idle1.png'),
                                    pygame.image.load('Moon_idle2.png'),
                                    pygame.image.load('Moon_idle3.png')],
                           'walk': [pygame.image.load('Moon_walk0.png'),
                                    pygame.image.load('Moon_walk1.png'),
                                    pygame.image.load('Moon_walk2.png'),
                                    pygame.image.load('Moon_walk3.png'),
                                    pygame.image.load('Moon_walk4.png'),
                                    pygame.image.load('Moon_walk5.png')],
                           'jump': [pygame.image.load('Moon_jump3.png')],
                           'fall': [pygame.image.load('Moon_fall0.png')]}
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.status = 'idle'

        # movements
        self.sens = '0'
        self.saut = False
        self.fall = False
        self.speed = 10
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 0.8
        self.jump_speed = -16

    def get_input(self):
        """touches de déplacements"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.sens = 'droite'
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.sens = 'gauche'
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pygame.K_UP]:
            if not self.saut:
                self.jump()

    def animate(self):
        """fait l'animation en fonction de la direction du personnage (s'il regarde à gauche ou à droite)"""
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.sens == 'gauche':
            self.image = image
        else:
            flipped = pygame.transform.flip(image, True, False)
            self.image = flipped

    def get_status(self):
        """définit si le joueur saute, tombe, marche ou reste immobile"""
        if self.direction.y > 1:
            self.status = 'fall'
        elif self.direction.y < 0:
            self.status = 'jump'
        else:
            if self.direction.x != 0:
                self.status = 'walk'
            else:
                self.status = 'idle'
            self.saut = False

    def apply_gravity(self):
        """applique la gravité"""
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        """fait sauter le personnage"""
        self.saut = True
        self.direction.y = self.jump_speed

    def update(self):
        self.get_status()
        self.get_input()
        self.animate()
