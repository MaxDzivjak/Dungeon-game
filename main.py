import pygame
import sys
from settings import *
from player import *
from wall import *
from gem import *
from gameObject import *


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

def create_gems(number_of_gems, walls_group):
    gems = pygame.sprite.Group()
    
    while len(gems) < number_of_gems:
        x = random.randint(0, WIDTH - 30)
        y = random.randint(0, HEIGHT - 30)
        
        new_gem = Gem(x, y)
        gems.add(new_gem)
        
        if not pygame.sprite.spritecollideany(new_gem, walls_group):
            gems.add(new_gem)
            
    return gems

# Vytvoření hráče (souřadnice x, y, šířka, výška, rychlost)
player = Player(400, 300, 50, 50, 5)
gems = create_gems(5, walls)

# 3. HLAVNÍ SMYČKA
running = True
while running:
    # --- 2. ZPRACOVÁNÍ UDÁLOSTÍ ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- 3. LOGIKA ---
    player.move(walls)
    collected_gems = pygame.sprite.spritecollide(player, gems, True)
    
    for gem in collected_gems:
        print("gem collected!")

    # --- 4. VYKRESLOVÁNÍ ---
    # Nejdřív pozadí, pak hráč
    screen.blit(bg_image, (0, 0))
    walls.draw(screen)
    screen.blit(bg_image, (0, 0))
    walls.draw(screen)
    gems.draw(screen) 
    screen.blit(player.image, player.rect)
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    
    # --- 5. ČASOVÁNÍ ---
    clock.tick(FPS)

pygame.quit()
sys.exit()