import pygame
from random import randint


def transform_image(image):
    return pygame.transform.scale(image[0], image[1])


class Shooter(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/sprites/zombie/pixil-frame-0.png")
        self.image = pygame.transform.scale(self.image, [100, 100])

        self.rect = pygame.Rect(-50, randint(0, 500), 60, 100)

        self.sprites = [
            pygame.image.load("data/sprites/shooter/pixil-frame-0.png").convert_alpha(),
            pygame.image.load("data/sprites/shooter/pixil-frame-1.png").convert_alpha(),
            pygame.image.load("data/sprites/shooter/pixil-frame-2.png").convert_alpha()
        ]
        self.index = 0

        self.speed = 3
        self.animation = True

        self.frame_rate = 10

        self.can_shoot = False
        self.shoot_index = 0

    def shoot(self, _class, _group):
        new_shot = _class(_group)
        new_shot.side = 1
        new_shot.rect.y = self.rect.y + 55
        new_shot.rect.x = self.rect.x + 100

    def animation_control(self):
        if self.rect.x > 200:
            self.animation = False

        if self.animation:
            self.index += 1

            if self.index > self.frame_rate:
                self.image = transform_image([self.sprites[1], [100, 100]])

                if self.index > self.frame_rate * 2:
                    self.image = transform_image([self.sprites[2], [100, 100]])

                    if self.index > self.frame_rate * 3:
                        self.index = 0
        else:
            self.image = transform_image([self.sprites[0], [100, 100]])

    def shoot_control(self):
        self.shoot_index += 1
        print(self.shoot_index)

        if self.shoot_index > 60:
            self.can_shoot = True
            self.shoot_index = 0

        else:
            self.can_shoot = False

    def update(self, *args):
        if self.animation:
            self.rect.x += self.speed
        else:
            pass

        self.animation_control()
        self.shoot_control()
