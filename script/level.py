import pygame
from tiles import Tile, Win
from settings import *
from players import Moon, Sun

class Level():
    """ prend les différents 'sprite' et les implémentes dans le jeu"""
    def __init__(self, level_data, surface):
        # level set up
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.win = pygame.sprite.Group()
        self.moon = pygame.sprite.GroupSingle()
        self.sun = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == 'W':
                    win_sprite = Win((x, y), tile_size)
                    self.tiles.add(win_sprite)
                if cell == 'M':
                    moon_sprite = Moon((x, y), self.display_surface)
                    self.moon.add(moon_sprite)
                if cell == 'S':
                    sun_sprite = Sun((x, y), self.display_surface)
                    self.sun.add(sun_sprite)

    def win_collision(self):
        if self.win.rect.colliderect(moon.rect) and self.win.rect.colliderect(sun.rect):
            sys.exit()

    def horizontal_movement_collision_m(self):
        moon = self.moon.sprite
        moon.rect.x += moon.direction.x * moon.speed

        for sprite_m in self.tiles.sprites():
            if sprite_m.rect.colliderect(moon.rect):
                if moon.direction.x < 0:
                    moon.rect.left = sprite_m.rect.right
                elif moon.direction.x > 0:
                    moon.rect.right = sprite_m.rect.left

    def vertical_movement_collision_m(self):
        moon = self.moon.sprite
        moon.apply_gravity()

        for sprite_m in self.tiles.sprites():
            if sprite_m.rect.colliderect(moon.rect):
                if moon.direction.y > 0:
                    moon.rect.bottom = sprite_m.rect.top
                    moon.direction.y = 0
                elif moon.direction.y < 0:
                    moon.rect.top = sprite_m.rect.bottom
                    moon.direction.y = 0

    def horizontal_movement_collision_s(self):
        sun = self.sun.sprite
        sun.rect.x += sun.direction.x * sun.speed

        for sprite_s in self.tiles.sprites():
            if sprite_s.rect.colliderect(sun.rect):
                if sun.direction.x < 0:
                    sun.rect.left = sprite_s.rect.right
                elif sun.direction.x > 0:
                    sun.rect.right = sprite_s.rect.left

    def vertical_movement_collision_s(self):
        sun = self.sun.sprite
        sun.apply_gravity()

        for sprite_s in self.tiles.sprites():
            if sprite_s.rect.colliderect(sun.rect):
                if sun.direction.y > 0:
                    sun.rect.bottom = sprite_s.rect.top
                    sun.direction.y = 0
                elif sun.direction.y < 0:
                    sun.rect.top = sprite_s.rect.bottom
                    sun.direction.y = 0

    def run(self):
        # level tiles
        self.tiles.draw(self.display_surface)

        # players
        self.moon.update()
        self.horizontal_movement_collision_m()
        self.vertical_movement_collision_m()
        self.moon.draw(self.display_surface)
        self.sun.update()
        self.horizontal_movement_collision_s()
        self.vertical_movement_collision_s()
        self.sun.draw(self.display_surface)