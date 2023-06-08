import WConio2 as WConio2
from Color import *

class Store:

    cor = Color()

    def __init__(self, posX, posY, character, color):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.character = color + character + self.cor.Color_Off


    