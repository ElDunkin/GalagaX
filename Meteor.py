import os
import pygame, random

from config import BLACK, HEIGHT, IMAGE_DIR, WIDTH

meteor_images = []

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(meteor_images)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-140, -100)
        self.speedy = random.randrange(1, 10)
        self.speedx = random.randrange(-5, 5)
        
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        
        if self.rect.top > HEIGHT + 10 or self.rect.left < -40 or self.rect.right > WIDTH + 40:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-140, -100)
            self.speedy = random.randrange(1, 10)
    def load_meteor():
        meteor_list = ["meteor_big1.png", "meteor_big2.png",
				"meteor_med1.png", "meteor_med2.png", "meteor_small1.png", "meteor_small2.png",
				"meteor_tiny1.png", "meteor_tiny2.png"]
        for img in meteor_list:
            meteor_images.append(pygame.image.load(os.path.join(IMAGE_DIR, img)).convert())

