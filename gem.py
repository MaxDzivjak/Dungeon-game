import pygame
from gameObject import GameObject

class Gem(GameObject):
    def __init__(self, x , y):
        super().__init__(x, y, 50, 50, "assets/gem.png")
        