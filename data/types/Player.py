import pygame


def transform_image(image, scale: tuple, flip_x: bool, flip_y: bool):
    return pygame.transform.flip(
        pygame.transform.scale(
            image,
            scale
        ), flip_x, flip_y
    )


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        # image
        self.width, self.height = 100, 100

        self.image = pygame.image.load("data/sprites/player/pixil-frame-0.png")
        self.image = pygame.transform.scale(self.image, [self.width, self.height])

        # rect
        self.rect = pygame.Rect(690, 600/2 - 100, 60, 95)

        self.speed = 8

        # properties
        self.kills = 0
        self.bullets = 16
        self.hp = 100
        self.coins = 0

        # animation
        self.sprites = [
            pygame.image.load("data/sprites/player/pixil-frame-0.png").convert_alpha(),
            pygame.image.load("data/sprites/player/pixil-frame-1.png").convert_alpha(),
            pygame.image.load("data/sprites/player/pixil-frame-2.png").convert_alpha()
        ]

        self.in_move = 0
        self.index = 0
        self.frame_rate = 5

        # difficulty
        self.difficulty_index = 10

        # guns
        self.guns = {
            "classic pistol": "blé"
        }
        self.selected_gun = self.guns["classic pistol"]

    def movement_control(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.in_move = 1

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.in_move = 1

        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.in_move = 1

        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.in_move = 1

        else:
            self.in_move = 0

    def animation_control(self):
        if self.in_move:
            self.index += 1

        else:
            self.index = 0
            self.image = transform_image(self.sprites[0], (100, 100), False, False)

        if self.index > self.frame_rate:
            self.image = transform_image(self.sprites[1], (100, 100), False, False)

            if self.index > self.frame_rate * 2:
                self.image = transform_image(self.sprites[2], (100, 100), False, False)

                if self.index > self.frame_rate * 3:
                    self.index = 0

    def update(self, *args):
        self.movement_control()
        self.animation_control()

        if self.rect.y > 500:
            self.rect.y = 500

        elif self.rect.y < -5:
            self.rect.y = -5

        if self.rect.x > 770:
            self.rect.x = 770

        elif self.rect.x < -10:
            self.rect.x = -10

        if self.hp <= 0:
            self.kill()
            self.hp = 0
