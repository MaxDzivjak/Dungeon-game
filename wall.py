import pygame
import random
from gameObject import GameObject
from settings import *

class Wall(GameObject):
    def __init__(self, x, y, width, height, image_path):
        super().__init__(x, y, width, height, image_path)

        width = random.randint(20, 100)
        height = random.randint(20, 100)


        self.image = pygame.Surface((width, height))
        gray_value = random.randint(100, 150)
        self.image.fill((gray_value, gray_value, gray_value))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - width)
        self.rect.y = random.randint(0, HEIGHT - height)