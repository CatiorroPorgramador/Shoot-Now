import pygame


class Shot(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.Surface([10, 5])
        self.image.fill((255, 235, 13))

        self.rect = pygame.Rect(0, 0, 10, 5)

        self.speed = 30

        self.side = 0

    def update(self, *args):
        if self.side:
            self.rect.x += self.speed

            if self.rect.x < -200:
                self.kill()

        else:
            self.rect.x -= self.speed

            if self.rect.x > 900:
                self.kill()
