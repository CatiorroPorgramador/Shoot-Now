import pygame
from random import randint, random

class Coin(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        
        self.n = randint(100, 750) + random();self.flag = True;self.stopRandom = randint(5*10, 50*10)
        self.image = pygame.image.load("")
        self.image = pygame.transform.scale(self.image, [25, 25])
        self.rect = pygame.Rect(self.n, 0, 25, 25)
        self.speed = 2
        self.timeLife = 600

    def update(self, *args):
        if self.flag == True:
          if self.rect.y >= self.stopRandom:
            self.flag = False
          self.rect.y += self.speed
        elif self.flag == False:
            self.timeLife -= 1
            if self.timeLife <= 0:
                self.kill()