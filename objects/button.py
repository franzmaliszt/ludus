import pygame
from utils import load_image


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.pos = pygame.math.Vector2(x, y)
        self.size = pygame.math.Vector2(width, height)
        self.image = load_image('roll', self.size)
        self.rect = self.image.get_rect()

    def update(self):
        pass
