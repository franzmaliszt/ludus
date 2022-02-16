import os
import pygame
from pygame import Surface

from config import ASSETS_DIR, WIN_WIDTH, WIN_HEIGHT, TITLE
from events import CUSTOM_EVENTS


def load_image(image_name: str, size) -> Surface:
    image = pygame.image.load(os.path.join(ASSETS_DIR, '{}.png').format(image_name))
    image = pygame.transform.scale(image, size)

    return image


def post_event(custom_event):
    event = pygame.event.Event(CUSTOM_EVENTS[custom_event])
    pygame.event.post(event)


def create_window():
    pygame.display.set_caption(TITLE)
    return pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
