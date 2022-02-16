import pygame

from objects import Secutor, Scene, Button
from fight import FightMotor

from utils import load_image


class BattleScene(Scene):
    def __init__(self, director):
        super().__init__()
        self.director = director
        self.agents = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        self.fightMotor = FightMotor
        self.size = self.director.screen.get_size()
        self.image = load_image('arena', self.size)

        gladiator1 = Secutor('Barzonidas', 300, 500)
        gladiator2 = Secutor('Levrex', 500, 500)
        button1 = Button(200, 100, 60, 60)

        self.agents.add(gladiator1)
        self.agents.add(gladiator2)
        self.buttons.add(button1)

        self.fightMotor = FightMotor(self.agents)
 
    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.director.quit_flag = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.director.quit()
                elif event.key == pygame.K_SPACE:
                    self.fightMotor.advance()

            # Check if any button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    for btn in self.buttons:
                        if btn.rect.collidepoint(mouse_pos):
                            self.fightMotor.advance()

    def update(self):
        self.agents.update()
        self.buttons.update()

    def render(self):
        self.director.screen.blit(self.image, pygame.math.Vector2(0, 0))
        self.agents.draw(self.director.screen)
        self.buttons.draw(self.director.screen)
