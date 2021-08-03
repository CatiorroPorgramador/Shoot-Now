import pygame
from random import randint


class Monster(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/sprites/monster/pixil-frame-0.png")
        self.image = pygame.transform.scale(self.image, [100, 100])

        self.rect = pygame.Rect(-50, randint(0, 500), 15, 10)

        self.sprites = [
            pygame.image.load("data/sprites/monster/pixil-frame-0.png"),
            pygame.image.load("data/sprites/monster/pixil-frame-1.png"),
        ]
        self.index = 0
        self.framerate = 10

        self.speed = 3

        self.hp = 2

    def transform_image(self, image):
        return pygame.transform.scale(image[0], image[1])

    def animation_control(self):
        self.index += 1

        if self.index > self.framerate:
            self.image = self.transform_image([self.sprites[0], [100, 100]])

            if self.index > self.framerate * 2:
                self.image = self.transform_image([self.sprites[1], [100, 100]])

                if self.index > self.framerate * 3:
                    self.index = 0

    def update(self, *args):
        self.rect.x += self.speed
        self.animation_control()

        if self.hp <= 0:
            self.kill()
