from objects import Dice


class FightMotor:
    def __init__(self, agents):
        self.attacker = None
        self.defender = None
        self.dice = Dice()

        for agent in agents:
            if self.attacker is None:
                self.attacker = agent
            else:
                self.defender = agent

    def advance(self):
        attacker = self.attacker
        defender = self.defender

        self.dice.roll()
        result = self.attacker.ruleset[self.dice.result]

        if 'damage' in result:
            defender.hp -= max(0, int(result[0]))
        elif 'heal' in result:
            attacker.hp = min(15, attacker.hp + int(result[0]))

        if defender.hp == 0:
            self.conclude()
        else:
            self.attacker = defender
            self.defender = attacker

        print('You rolled:', result)
        print(attacker.name, attacker.hp)
        print(defender.name, defender.hp)

    def conclude(self):
        print(self.attacker.name, 'wins!')
