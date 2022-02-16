import pygame
from objects import Scene
from config import FPS
from utils import create_window
from scenes import BattleScene


class Director:
    def __init__(self):
        self.screen = create_window()
        self.scene = None
        self.quit_flag = False
        self.clock = pygame.time.Clock()

    def launch(self):
        battle_scene = BattleScene(self)
        self.change_scene(battle_scene)

    def loop(self):
        while not self.quit_flag:
            self.clock.tick(FPS)

            self.scene.process_input()
            self.scene.update()
            self.scene.render()

            pygame.display.flip()

    def change_scene(self, scene: Scene):
        self.scene = scene

    def quit(self):
        self.quit_flag = True
