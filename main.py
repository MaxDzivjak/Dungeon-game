import pygame
import sys
from settings import *
from player import *
from wall import *


# 1. NASTAVENÍ SYSTÉMU (Vždycky první)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon game")
clock = pygame.time.Clock()

# 2. NAČTENÍ DAT (Až když běží pygame)
# Ujisti se, že se soubor jmenuje přesně background.jpg a je ve složce assets
bg_image = pygame.image.load("assets/background.jpg").convert()
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

walls = pygame.sprite.Group()
for i in range(8):
    new_wall = Wall()
    walls.add(new_wall)

# Vytvoření hráče (souřadnice x, y, šířka, výška, rychlost)
player = Player(400, 300, 50, 50, 5)

# 3. HLAVNÍ SMYČKA
running = True
while running:
    # --- 2. ZPRACOVÁNÍ UDÁLOSTÍ ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- 3. LOGIKA ---
    player.move(walls)

    # --- 4. VYKRESLOVÁNÍ ---
    # Nejdřív pozadí, pak hráč
    screen.blit(bg_image, (0, 0))
    walls.draw(screen)
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    
    # --- 5. ČASOVÁNÍ ---
    clock.tick(FPS)

pygame.quit()
sys.exit()