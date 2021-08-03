import pygame
from random import randint

class Zombie(pygame.sprite.Sprite):
	def __init__(self, *groups):
		super().__init__(*groups)

		self.image = pygame.image.load("data/sprites/zombie/pixil-frame-0.png")
		self.image = pygame.transform.scale(self.image, [100, 100])

		self.rect = pygame.Rect(-50, randint(0, 500), 60, 100)

		self.sprites = [
			pygame.image.load("data/sprites/zombie/pixil-frame-0.png").convert_alpha(),
			pygame.image.load("data/sprites/zombie/pixil-frame-1.png").convert_alpha(),
			pygame.image.load("data/sprites/zombie/pixil-frame-2.png").convert_alpha()
		]	
		self.index = 0
		self.framerate = 10

		self.speed = 3

	def transform_image(self, image):
		return pygame.transform.scale(image[0], image[1])

	def animation_control(self):
		self.index += 1

		if self.index > self.framerate:
			self.image = self.transform_image([self.sprites[1], [100, 100]])

			if self.index > self.framerate*2:
				self.image = self.transform_image([self.sprites[2], [100, 100]])

				if self.index > self.framerate*3:
					self.index = 0


	def update(self, *args):
		self.rect.x += self.speed

		self.animation_control()