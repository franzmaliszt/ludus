import pygame
from objects import Director


def main():
    director = Director()
    director.launch()
    director.loop()


if __name__ == '__main__':
    pygame.init()
    main()
