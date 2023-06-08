import os
from random import *
import WConio2 as WConio2
from FileManager import File
from Character import *
from Player import Player
from Store import Store
from Rock import *
from Level import *
from Interactable import Interactable
from MenuController import Controller
from Color import *

class System:

    gameState = 0
    frameCont = 0
    contPickaxe = 1

    starterHour = 8
    
    day = 0
    hour = starterHour
    minute = 0

    closestRock = 0
    closestRockObject = 0
    rockLife = 0

    level = 0
    highestLevel = 1

    minedRocks = 0

    rocksInScene = []

    timeStopped = True

    nick = ''

    cor = Color()

    test = False

    score = 0
     
    playerCanMine = False

    enemyOnScene = False

    def __init__(self, screenSizeX, screenSizeY):
        self.screenSizeX = screenSizeX
        self.screenSizeY = screenSizeY
        self.player = Player(1, self.screenSizeY - 2, "██", self.cor.BLUE)
        self.store = Store(0, self.screenSizeY - 1, "▀█", self.cor.GREEN)
        self.northEntrance = Interactable(screenSizeX/2 - 2, 0, "▀▀", self.cor.BLACK)
        self.southEntrance = Interactable(screenSizeX/2 - 2, self.screenSizeY - 1, "▄▄", self.cor.BLACK)
        self.enemy = Character(-5, -5, "██", self.cor.RED)
        self.fileManager = File()
        self.fileManager.createHighScores()
        self.menuController = Controller(self.checkMenuOpts(), 3, False)
        self.storeController = Controller(0, 3, True)

    def Update(self):
        self.player.playerMovement()
        if self.player.goToMenu:
            self.menuController.starterOpt = self.checkMenuOpts()
            self.gameState = 0
            self.player.goToMenu = False
        self.playerCanMine = self.checkCloseRocks()

        if self.playerCanMine and self.player.hasMined:
            self.player.hasMined = False
            if len(self.rocksInScene) != 0:
                if not self.rocksInScene[self.closestRock].damageRock(self.player.pickDamage):
                    self.player.money += self.rocksInScene[self.closestRock].value
                    self.minedRocks += 1
                    del self.rocksInScene[self.closestRock]
        
        self.player.hasMined = False

        self.clearedLevel = len(self.rocksInScene) == 0

        if self.clearedLevel and (self.player.posX == self.northEntrance.posX and self.player.posY == self.northEntrance.posY):
            if self.level >= self.highestLevel:
                self.level += 1
            else:
                self.level = self.highestLevel
            if self.level % 5 == 0:
                self.highestLevel = self.level
            self.player.posX = self.southEntrance.posX
            self.player.posY = self.southEntrance.posY - 1
            if self.level != 0 and self.level >= self.highestLevel:
                self.generateRocks(self.rockLife)
            self.timeStopped = False

        if self.player.posX == self.southEntrance.posX and self.player.posY == self.southEntrance.posY and self.level != 0:
            self.goToBase()
        
        if not self.enemyOnScene:
            self.enemy.posX = -5
            self.enemy.posY = -5        

        if self.enemyCollision() == True:
            self.gameState = 2
        self.frameCont += 1

        if self.level == 0:
            if self.player.isBuying and self.canBuy():
                self.openStore()
        
        self.player.isBuying = False
            
        if self.frameCont % 32 == 0:
            self.delayUpdate()
        elif self.frameCont % 14 == 0:
            self.enemyUpdate()

    def goToBase(self):
        self.enemyOnScene = False
        self.timeStopped = True
        arr = []
        self.rocksInScene = arr
        self.player.posX = self.northEntrance.posX
        self.player.posY = self.northEntrance.posY + 1
        self.hour = self.starterHour - self.player.dayDuration
        self.minute = 0
        self.day += 1
        self.level = 0
        self.fileManager.saveGame(self.highestLevel, self.player.money, self.player.pickDamage, self.player.dayDuration, self.day, self.contPickaxe, self.minedRocks, self.player.luck)

    def delayUpdate(self):
        self.countHours()
    
    def enemyUpdate(self):
        if self.enemyOnScene:
            if self.enemy.posX > self.player.posX:
                self.enemy.posX -= 1 
            elif self.enemy.posX == self.player.posX:
                self.enemy.posX = self.enemy.posX
            else:
                self.enemy.posX += 1
            if self.enemy.posY > self.player.posY:
                self.enemy.posY -= 1
            elif self.enemy.posY == self.player.posY:
                self.enemy.posY = self.enemy.posY
            else:
                self.enemy.posY += 1    

    def storeUpdate(self):
        self.storeController.playerSelection()
        if self.storeController.closedStore:
            self.closeStore()
        if self.storeController.opt == 0 and self.storeController.hasSelected:
            self.upgradePickaxe()
        if self.storeController.opt == 1 and self.storeController.hasSelected:
            self.upgradeLuck()
        if self.storeController.opt == 2 and self.storeController.hasSelected:
            self.upgradeDayDuration()
        elif self.storeController.opt == 3 and self.storeController.hasSelected:
            self.closeStore()
        self.storeController.hasSelected = False
        
    def menuUpdate(self):
        self.menuController.playerSelection()
        if self.menuController.opt == 0 and self.menuController.hasSelected:
            self.continueGame()
        if self.menuController.opt == 1 and self.menuController.hasSelected:
            self.newGame()
        if self.menuController.opt == 2 and self.menuController.hasSelected:
            self.showHighscore()
        if self.menuController.opt == 3 and self.menuController.hasSelected:
            os.system("cls")
            exit()
        self.menuController.hasSelected = False
        
    def gameOverUpdate(self):
        if len(self.nick) < 3:
            if WConio2.kbhit():
                (key, symbol) = WConio2.getch()
                self.nick += symbol
                self.score = (self.minedRocks + self.player.money) * self.contPickaxe
                i = 0
                if len(self.nick) >= 3:
                    for score in self.fileManager.readHighScore():
                        place = score.split('-')
                        if self.score > int(place[1]):
                            self.fileManager.setHighScore(i, self.nick, self.score)
                            return
                        i += 1
        else:
            if WConio2.kbhit():
                (key, symbol) = WConio2.getch()
                if symbol == ' ':
                    self.showHighscore()
                    self.fileManager.deleteSave()
                    self.menuController.starterOpt = self.checkMenuOpts()

    def enemyCollision(self):
        if self.player.posX == self.enemy.posX and self.player.posY == self.enemy.posY:
            return True
    
    def checkCloseRocks(self):
        rockIndex = -1
        player = self.player
        for rock in self.rocksInScene:
            rockIndex += 1
            distX = player.posX - rock.posX
            distY = player.posY - rock.posY
            if (distX >= -1 and distX <= 1) and (distY >= -1 and distY <=1):
                self.closestRock = rockIndex
                self.closestRockObject = rock
                return True
        return False

    def restartMenu(self):
        if WConio2.kbhit():
            (key, symbol) = WConio2.getch()
            if symbol == ' ':
                self.gameState = 0

    def countHours(self):
        if not self.timeStopped:   
            self.minute += 1
            if self.minute >= 60:
                self.minute = 0
                self.hour += 1
                if self.hour >= 24:
                    self.timeStopped = True
                    self.spawnEnemy()
                    self.hour = 0
                    self.minute = 0
                    self.day += 1

    def generateRocks(self, rockLife):
        vidaBase = 1
        aumentoDeVida = 0.5
        if self.level % 5 == 0:
            aumentoDeVida *= 2 + (self.level/5)
        
        self.rockLife = rockLife
        if self.level == 1:
            rockLife = vidaBase
        else:
            rockLife = vidaBase + (aumentoDeVida * self.level)
        for i in range(randint(8, 22)):
            ouroInScene = 0
            esmeraldaInScene = 0
            rubiInScene = 0
            diamanteInScene = 0

            chanceOuro = randint(1,10)
            chanceEsmeralda = randint(1,25)
            chanceRubi = randint(1,50)
            chanceDiamante = randint(1,100)

            if chanceOuro <= self.player.luck and self.level >= 5:
                ouroInScene += 1
                if ouroInScene < 6 :
                    ouro = Rock("ouro", "██", self.cor.GOLD, int(rockLife)*2)
                    ouro.value = 20
                    self.rocksInScene.append(ouro)
            if chanceEsmeralda <= self.player.luck and self.level >= 25:
                esmeraldaInScene += 1
                esmeralda = Rock("esmeralda", "██", self.cor.EMERALD, int(rockLife)*3)
                esmeralda.value = 35
                if esmeraldaInScene < 4:
                    self.rocksInScene.append(esmeralda)
            if chanceRubi <= self.player.luck and self.level >= 50:
                rubiInScene += 1
                rubi = Rock("rubi", "██", self.cor.RUBY, int(rockLife)*4)
                rubi.value = 120
                if rubiInScene < 3:
                    self.rocksInScene.append(rubi)
            if chanceDiamante <= self.player.luck and self.level >= 75:
                diamanteInScene += 1
                diamante = Rock("diamante", "██", self.cor.DIAMOND, int(rockLife)*5)
                diamante.value = 1000
                if diamanteInScene < 2:
                    self.rocksInScene.append(diamante)
            
            rock = Rock("pedra", "██", self.cor.GRAY, int(rockLife))
            self.rocksInScene.append(rock)

    def spawnEnemy(self):
        self.enemy.posX = self.northEntrance.posX
        self.enemy.posY = self.northEntrance.posY
        self.enemyOnScene = True

    def canBuy(self):
        player = self.player
        store = self.store
        distX = player.posX - store.posX
        distY = player.posY - store.posY
        if (distX >= -1 and distX <= 1) and (distY >= -1 and distY <=1):
            return True
        else:
            return False

    def openStore(self):
        self.player.isBuying = False
        self.gameState = 3
    
    def resetScene(self):
        self.timeStopped = True
        self.rocksInScene = [] 
        self.level = 0
        self.enemyOnScene = False
        self.minute = 0
        self.enemy.posX = -5
        self.enemy.posY = -5
        self.nick = ''
        self.score = 0
        self.highestLevel = 1
        self.player.money = 0
        self.player.pickDamage = 1
        self.player.dayDuration = 0
        self.hour = self.starterHour - self.player.dayDuration
        self.day = 0
        self.contPickaxe = 1
        self.minedRocks = 0
        self.player.posX = 1
        self.player.posY = self.screenSizeY - 2
        self.player.luck = 1

    def continueGame(self):
        self.resetScene()
        save = self.fileManager.readSave()
        self.player.posX = self.northEntrance.posX
        self.player.posY = self.northEntrance.posY + 1
        self.highestLevel = int(save[0])
        self.player.money = int(save[1])
        self.player.pickDamage = int(save[2])
        self.player.dayDuration = int(save[3])
        self.day = int(save[4])
        self.contPickaxe = int(save[5])
        self.minedRocks = int(save[6])
        self.player.luck = int(save[7])
        self.hour = self.starterHour - self.player.dayDuration
        self.gameState = 1

    def newGame(self):
        self.resetScene()
        self.gameState = 1

    def showHighscore(self):
        self.gameState = 4
        
    def upgradePickaxe(self):
        if self.player.money >= self.player.pickDamage:
            self.player.money -= self.player.pickDamage
            self.player.pickDamage *= 2
            self.contPickaxe +=1
    
    def upgradeLuck(self):
        if self.player.luck >= 5:
            return
        if self.player.money >= 500:
            self.player.money -= 500
            self.player.luck += 1

    def upgradeDayDuration(self):
        if self.player.dayDuration >= 3:
            return
        if self.player.money >= 100:
            self.player.money -= 100
            self.player.dayDuration += 1

    def closeStore(self):
        self.gameState = 1
        self.hour = self.starterHour - self.player.dayDuration
        self.storeController.closedStore = False

    def checkMenuOpts(self):
        if self.fileManager.hasSaveFile():
            return 0
        else:
            return 1
        
    
        