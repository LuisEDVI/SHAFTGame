import WConio2 as WConio2
from Color import *

class Player:

    cor = Color()

    posX = 0
    posY = 0
    hasMined = False
    isBuying = False
    goToMenu = False

    pickDamage = 1
    dayDuration = 0
    luck = 1
    money = 0
    
    def __init__(self, posX, posY, character, color):
        self.setPosition(posX, posY)
        self.color = color
        self.character = color + character + self.cor.Color_Off

    def setPosition(self, x, y):
        self.posX = x
        self.posY = y


    def playerMovement(self): 
        if WConio2.kbhit():
            (key, symbol) = WConio2.getch()
            if symbol == 'a' and (self.posX > 0):
                self.posX -= 1
            if symbol == 'd' and (self.posX < 25):
                self.posX += 1
            if symbol == 'w' and (self.posY > 0):
                self.posY -= 1
            if symbol == 's' and (self.posY < 27):
                self.posY += 1
            if symbol == " ":
                self.hasMined = not self.hasMined
            if symbol == "p":
                self.isBuying = True
            if symbol == "'":
                self.goToMenu = True
