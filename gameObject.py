import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y