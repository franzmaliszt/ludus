import pygame

from utils import load_image
from objects import Scene


class MainMenu(Scene):
    def __init__(self):
        super().__init__()
        self.buttons = pygame.sprite.Group()
        self.image = load_image('mainmenu', self.size)
        pass

    def process_input(self):
        pass

    def update(self):
        pass

    def render(self):
        pass
