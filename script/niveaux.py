import pygame
from start_window import *
def niveaux():
    if lvl == '0':
        level_map = level_map0
    if lvl == '1':
        level_map = level_map1
    if lvl == '2':
        level_map = level_map2
    if lvl == '3':
        level_map = level_map3
    if lvl == '4':
        level_map = level_map4