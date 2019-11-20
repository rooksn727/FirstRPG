import Game


class Enemy:
    def __init__(self, HP, DMG, skin_color, name):
        self.HP  = HP
        self.DMG = DMG
        self.skin_color = skin_color
        self.name = name

    def attack(self):
        print(self.name + " hit you for " + str(self.DMG) + "hitpoints")
        return self.DMG

    def observe(self):
        print("The man has the name " + self.name + "on his shirt and has " + self.skin_color)


