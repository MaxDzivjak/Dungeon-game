import pygame
import sys
import random
from settings import *
from player import *
from wall import *
from gem import *
from gameObject import *

MENU = "menu"
GAME = "game"
END = "end"

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Game")
clock = pygame.time.Clock()

#background
bg_image = pygame.image.load("assets/ground.png").convert()
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

#screen
def draw_menu(screen):
    screen.fill((30, 30, 30))
    font = pygame.font.SysFont("Arial", 64)
    text = font.render("Dungeon Game", True, (255, 215, 0))
    screen.blit(text, (WIDTH//2 - text.get_width()//2, 200))
    
    font_small = pygame.font.SysFont("Arial", 32)
    start_text = font_small.render("Press space to start", True, (255, 255, 255))
    screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, 400))

def draw_end_screen(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("Arial", 64)
    text = font.render("Game over", True, (255, 0, 0))
    screen.blit(text, (WIDTH//2 - text.get_width()//2, 250))
    
    font_small = pygame.font.SysFont("Arial", 24)
    restart_text = font_small.render("Press R to restart", True, (200, 200, 200))
    screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, 400))

#Gems
def create_gems(number_of_gems, walls_group):
    gems = pygame.sprite.Group()
    while len(gems) < number_of_gems:
        x = random.randint(0, WIDTH - 30)
        y = random.randint(0, HEIGHT - 30)
        new_gem = Gem(x, y)
        if not pygame.sprite.spritecollideany(new_gem, walls_group):
            gems.add(new_gem)
    return gems

#Objects
def reset_game():
    walls = pygame.sprite.Group()
    number_of_walls = 8
    
    while len(walls) < number_of_walls:
        w = random.randint(40, 150)
        h = random.randint(40, 150)
        
        x = random.randint(0, WIDTH - w)
        y = random.randint(0, HEIGHT - h)
        
        new_wall = Wall(x, y, w, h, "assets/wall.png")
        
        player_start_rect = pygame.Rect(350, 250, 100, 100)
        
        if not new_wall.rect.colliderect(player_start_rect):
            walls.add(new_wall)
    
    gems = create_gems(5, walls)
    player = Player(400, 300, 50, 50, 5)
    return player, walls, gems

#Initialize
player, walls, gems = reset_game()
game_state = MENU
running = True

#Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if game_state == MENU and event.key == pygame.K_SPACE:
                game_state = GAME
            if game_state == END and event.key == pygame.K_r:
                player, walls, gems = reset_game() # Všechno vygenerujeme znova
                game_state = MENU

    if game_state == MENU:
        draw_menu(screen)
    
    elif game_state == GAME:
        player.move(walls)
        
        collected_gems = pygame.sprite.spritecollide(player, gems, True)
        for gem in collected_gems:
            print("Gem collected!")
        
        if len(gems) == 0:
            game_state = END
            
        screen.blit(bg_image, (0, 0))
        walls.draw(screen)
        gems.draw(screen) 
        screen.blit(player.image, player.rect)

    elif game_state == END:
        draw_end_screen(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()