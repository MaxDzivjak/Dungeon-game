import pygame
from gameObject import GameObject
from settings import *

class Wall(GameObject):
    def __init__(self, x, y, width, height):
        image_path = "assets/wall.png"
        super().__init__(x, y, width, height, image_path)