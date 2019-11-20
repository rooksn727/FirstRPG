

class Me:
    def __init__(self, HP, DMG, STMNA, Money):
        self.HP = HP
        self.DMG = DMG
        self.STMNA = STMNA
        self.Money = Money

    def dead(self):
        print("Game over")

    def attack(self):
        print("You hit your foe for ", self.DMG)

