from Color import *

class Character:

    def __init__(self, posX, posY, character, color):
        self.posX = posX
        self.posY = posY
        self.character = character
        self.character = color + character + Color.Color_Off

    #def setColor(color):
        #return color 
    