import pygame

from menu import *
import Explosion
import Meteor
from Player import Player
from menu import draw_shield_bar, draw_text, show_go_screen

class GameOver():
    
    game_over = True
    running = True
    while running:
        if game_over:
        
            show_go_screen()
        
            game_over = False
            all_sprites = pygame.sprite.group()
            meteor_list = pygame.sprite.group()
            bullets = pygame.sprite.group()
        
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
                    player.shoot()
                
        all_sprites.update()

        hits = pygame.sprite.groupcollide(meteor_list, bullets, True, True)
        for hit in hits:
            score += 10
            explosion_sound.play()
            explosion = Explosion(hit.rect.center)
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