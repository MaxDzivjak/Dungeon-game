import pygame
import GameObject

class Player(GameObject):
    
    def __init__(self, x, y, width, height, image_path = None, speed = None):
        self.image = pygame.image.load("assets/miner.jpg").convert_alpha()
        super().__init__(x, y, width, height, image_path, speed)

        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y

        self.speed = speed


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_s]:
            self.rect.y -= self.speed
        if keys[pygame.K_w]:
            self.rect.y += self.speed

        
