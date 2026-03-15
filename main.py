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
GAME_TIME = 15
start_ticks = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Game")
clock = pygame.time.Clock()

#background
bg_image = pygame.image.load("assets/ground.png").convert()
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

fog = pygame.Surface((WIDTH, HEIGHT))
fog.fill((0, 0, 0))
fog.set_alpha(255)

#screen
def draw_menu(screen):
    screen.fill((30, 30, 30))
    font = pygame.font.SysFont("Nexa", 64)
    text = font.render("Dungeon Game", True, (255, 215, 0))
    screen.blit(text, (WIDTH//2 - text.get_width()//2, 200))
    
    font_small = pygame.font.SysFont("Nexa", 32)
    start_text = font_small.render("Press space to start", True, (255, 255, 255))
    screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, 400))

def draw_end_screen(screen, win):
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("Nexa", 64)
    
    if win:
        text = font.render("Victory!", True, (0, 139, 139))
        sub_text_str = "All gems collected!"
    else:
        text = font.render("Game Over", True, (255, 64, 64))
        sub_text_str = "Time's up!"

    screen.blit(text, (WIDTH//2 - text.get_width()//2, 250))
    
    font_small = pygame.font.SysFont("Nexa", 32)
    sub_text = font_small.render(sub_text_str, True, (255, 255, 255))
    screen.blit(sub_text, (WIDTH//2 - sub_text.get_width()//2, 330))
    
    restart_text = font_small.render("Press R to restart", True, (200, 200, 200))
    screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, 450))

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
    global start_ticks
    start_ticks = pygame.time.get_ticks()
    walls = pygame.sprite.Group()
    number_of_walls = 8
    
    while len(walls) < number_of_walls:
        w = random.randint(40, 150)
        h = random.randint(40, 150)
        x = random.randint(0, WIDTH - w)
        y = random.randint(0, HEIGHT - h)
        
        new_wall = Wall(x, y, w, h)
        
        player_start_rect = pygame.Rect(350, 250, 100, 100)
        if not new_wall.rect.colliderect(player_start_rect):
            walls.add(new_wall)
    
    gems = create_gems(5, walls)
    player = Player(400, 300, 80, 80, 3)
    return player, walls, gems

#Game loop
player, walls, gems = reset_game() 
game_state = MENU
won = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if game_state == MENU and event.key == pygame.K_SPACE:
                game_state = GAME
            if game_state == END and event.key == pygame.K_r:
                player, walls, gems = reset_game()
                won = False
                game_state = MENU

    if game_state == MENU:
        draw_menu(screen)
    
    elif game_state == GAME:
        seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000
        time_left = max(0, GAME_TIME - seconds_passed)

        if time_left <= 0:
            won = False
            game_state = END

        player.move(walls)
        
        collected_gems = []
        for gem in gems:
            if player.hitbox.colliderect(gem.rect):
                gem.kill()
                collected_gems.append(gem)
        
        for gem in collected_gems:
            start_ticks += 2000
            print("Gem collected!")
        
        if len(gems) == 0:
            won = True
            game_state = END
            
        screen.blit(bg_image, (0, 0))
        walls.draw(screen)
        gems.draw(screen) 
        screen.blit(player.image, player.rect)
        
        # MLHA (jen v GAME módu)
        fog.fill((0, 0, 0))
        pygame.draw.circle(fog, (255, 255, 255), player.rect.center, 80)
        fog.set_colorkey((255, 255, 255))
        screen.blit(fog, (0, 0))
        
        # TEXTY (až nad mlhu!)
        font_timer = pygame.font.SysFont("Arial", 30)
        timer_color = (255, 255, 255) if time_left > 10 else (255, 0, 0)
        timer_text = font_timer.render(f"Time: {time_left}s", True, timer_color)
        screen.blit(timer_text, (20, 20))

    elif game_state == END:
        draw_end_screen(screen, won)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()