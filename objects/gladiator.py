import pygame

from config import GLADIATOR_WIDTH, GLADIATOR_HEIGHT


class Gladiator(pygame.sprite.Sprite):
    def __init__(self, name: str, x: int, y: int):
        super().__init__()
        self.name = name
        self.hp = 15

        self.pos = pygame.math.Vector2(x, y)
        self.size = pygame.math.Vector2(GLADIATOR_WIDTH, GLADIATOR_HEIGHT)
        self.image = None
        self.rect = None

    def update(self):
        pass
