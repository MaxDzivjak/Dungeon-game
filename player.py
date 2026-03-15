import pygame
from gameObject import GameObject
from settings import *
from wall import Wall

class Player(GameObject):
    def __init__(self, x, y, width, height, speed):
        super().__init__(x, y, width, height, "assets/miner.png")
        
        self.image_left = self.image
        self.image_right = pygame.transform.flip(self.image_left, True, False)
        self.speed = speed
        
        self.hitbox = self.rect.inflate(-40, -20)

    def move(self, walls):
        keys = pygame.key.get_pressed()
        old_x = self.rect.x
        old_y = self.rect.y

        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.image = self.image_left
        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed
            self.image = self.image_right
        
        self.hitbox.center = self.rect.center
        
        for wall in walls:
            if self.hitbox.colliderect(wall.rect):
                self.rect.x = old_x
                break

        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

        self.hitbox.center = self.rect.center
        
        for wall in walls:
            if self.hitbox.colliderect(wall.rect):
                self.rect.y = old_y
                break
        
        self.hitbox.center = self.rect.center

        
