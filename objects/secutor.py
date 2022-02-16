from objects import Gladiator
from utils import load_image


class Secutor(Gladiator):
    def __init__(self, name: str, x: int, y: int):
        Gladiator.__init__(self, name, x, y)
        self.image = load_image(self.name, self.size)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.ruleset = {
            1: "4 damage",
            2: "4 damage",
            3: "2 damage",
            4: "2 damage",
            5: "2 damage",
            6: "2 damage",
            7: "1 damage",
            8: "1 damage",
            9: "1 damage",
            10: "1 damage",
            11: "1 damage",
            12: "1 damage",
            13: "miss",
            14: "miss",
            15: "miss",
            16: "miss",
            17: "miss",
            18: "4 heal",
            19: "2 heal",
            20: "1 heal"
        }

    def update(self):
        pass
