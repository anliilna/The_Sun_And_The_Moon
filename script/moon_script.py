# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:11:14 2022

@author: anli.yamada
"""

import pygame

class Moon():
    def __init__(self):
        self.position = 400
        self.hauteur = 400
        self.vitesse = 15
        self.sens = '0'
        self.saut = False
        self.idle = [pygame.image.load('Moon_idle0.png'),
                     pygame.image.load('Moon_idle1.png'),
                     pygame.image.load('Moon_idle2.png'),
                     pygame.image.load('Moon_idle3.png')]
        self.idle_right = [pygame.image.load('Moon_idle_right0.png'),
                           pygame.image.load('Moon_idle_right1.png'),
                           pygame.image.load('Moon_idle_right2.png'),
                           pygame.image.load('Moon_idle_right3.png')]
        self.walk_left = [pygame.image.load('Moon_walk0.png'),
                          pygame.image.load('Moon_walk1.png'),
                          pygame.image.load('Moon_walk2.png'),
                          pygame.image.load('Moon_walk3.png'),
                          pygame.image.load('Moon_walk4.png'),
                          pygame.image.load('Moon_walk4.png'),
                          pygame.image.load('Moon_walk5.png')]
        self.walk_right = [pygame.image.load('Moon_walk_right0.png'),
                           pygame.image.load('Moon_walk_right1.png'),
                           pygame.image.load('Moon_walk_right2.png'),
                           pygame.image.load('Moon_walk_right3.png'),
                           pygame.image.load('Moon_walk_right4.png'),
                           pygame.image.load('Moon_walk_right5.png')]
        '''self.jump =
        self.push'''
        self.anim = self.idle

    def gravite(self):
        self.hauteur = self.hauteur + self.vitesse
        if self.hauteur >= 500:
            self.hauteur = 500

    def deplacer(self):
        if (self.sens == "droite") and (self.position < 1200):
            self.position = self.position + self.vitesse
        elif (self.sens == "gauche") and (self.position > 0):
            self.position = self.position - self.vitesse

    def sauter(self):
        if self.saut:
            self.hauteur -= 20