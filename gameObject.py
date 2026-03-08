import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image_path):
        super().__init__()
        
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y