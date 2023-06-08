from random import *
from Color import *

class Rock:

    cor = Color()

    value = 1
    lifePoints = 1

    def __init__(self, name, character, color, lifePoints, posX=None, posY=None):
        self.name = name
        self.posX = posX if posX else randint(2, 23)
        self.posY = posY if posY else randint(2, 25)
        self.lifePoints = lifePoints
        self.color = color
        self.character = color + character + self.cor.Color_Off

    def damageRock(self, damageTaken):
        self.lifePoints -= damageTaken
        if self.lifePoints <= 0:
            return False
        return True

        