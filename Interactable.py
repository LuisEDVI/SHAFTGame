from Color import *


class Interactable:

    cor = Color()

    canInteract = False

    def __init__(self, posX, posY, character, color):
        self.color = color
        self.character = color + character + self.cor.Color_Off
        self.posX = posX
        self.posY = posY