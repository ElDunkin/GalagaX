import os
import pygame, random

from Explosion import Explosion 
from Meteor import Meteor
from Player import Player
from config import BLACK, GREEN, HEIGHT, IMAGE_DIR, WHITE, WIDTH
from Bullet import Bullet

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
Explosion.load_explosion()
Meteor.load_meteor()
pygame.display.set_caption("GALAGA X")
clock = pygame.time.Clock()  

background = pygame.image.load(os.path.join(IMAGE_DIR,"background.png")).convert()
laser_sound = pygame.mixer.Sound(os.path.join(IMAGE_DIR, "laser5.ogg"))
explosion_sound = pygame.mixer.Sound(os.path.join(IMAGE_DIR, "explosion.wav"))
pygame.mixer.music.load(os.path.join(IMAGE_DIR, "music.ogg"))
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops =-1)

def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)
    
def draw_shield_bar(surface, x, y, percentage):
    BAR_LENGTH = 100    
    BAR_HEIGHT = 10
    fill_length = (percentage / 100) * BAR_LENGTH
    border = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill = pygame.Rect(x, y, fill_length, BAR_HEIGHT)
    pygame.draw.rect(surface, GREEN, fill)
    pygame.draw.rect(surface, WHITE, border, 2)
    
def show_go_screen():
    screen.blit(background,[0,0])
    draw_text(screen, "GALAGA X", 65, WIDTH // 2, HEIGHT // 4)
    draw_text(screen, "Derriba tantos asteroides como puedas.", 27, WIDTH // 2, HEIGHT // 2)
    draw_text(screen, "Presiona una tecla", 27, WIDTH //2, HEIGHT * 3/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

game_over = True
running = True
while running:
    if game_over:
        
        show_go_screen()
        game_over = False
        
        all_sprites = pygame.sprite.Group()
        meteor_list = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        
        player = Player()
        all_sprites.add(player)
        
        for i in range(8):
            meteor = Meteor()
            all_sprites.add(meteor)
            meteor_list.add(meteor)
            
        score = 0
        
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot(all_sprites, bullets, laser_sound)
                
    all_sprites.update()

    hits = pygame.sprite.groupcollide(meteor_list, bullets, True, True)
    for hit in hits:
        score += 1000
        explosion_sound.play()
        explosion = Explosion(hit.rect.center)
        all_sprites.add(explosion)
        meteor = Meteor()
        all_sprites.add(meteor)
        meteor_list.add(meteor)
        
    hits = pygame.sprite.spritecollide(player, meteor_list, True)
    for hit in hits:
        player.shield -= 25
        meteor = Meteor()
        all_sprites.add(meteor)
        meteor_list.add(meteor)
        if player.shield <= 0:
            game_over = True

    screen.blit(background, [0,0])

    all_sprites.draw(screen)
    
    draw_text(screen, str(score), 25, WIDTH // 2, 10)
    
    draw_shield_bar(screen, 5, 5, player.shield)
    
    pygame.display.flip()

pygame.quit()




