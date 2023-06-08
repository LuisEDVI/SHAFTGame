from os import system
from System import *
from Rock import *
import WConio2 as WConio2
from Color import *

class Screen:

    cor = Color()

    system = System(28,28)

    sizeY = system.screenSizeY
    sizeX = system.screenSizeX

    def gameHUD(self):
        #HUD
        system = self.system
        rock = self.system.closestRockObject
        if system.level == 0:
            print("Level: BASE (SAFE ZONE)")
        else:
            print("Level: " + str(system.level) + "                        ")
        if system.minute < 10:
            print("Dia: " + str(system.day) + " horário: " + str(system.hour) + ":" + "0" + str(system.minute) + ' ')
        else:
            print("Dia: " + str(system.day) + " horário: " + str(system.hour) + ":" + str(system.minute) + '  ')
        print("Dinheiro: " + str(system.player.money)+'        ')
        if system.playerCanMine:
            print("pressione ESPAÇO para minerar")
        elif self.system.level == 0 and system.canBuy() and self.system.gameState == 1:
            print("pressione P para acessar a loja")
        else:
            print("                                                                       ")
        if system.playerCanMine:
            print("Minério próximo: " + rock.name + ". Pontos de vida: " + str(rock.lifePoints) + ". Valor: R$ " + str(rock.value))
        else:
            print("                                                                       ")
    
    def hideHUD(self):
        for i in range(1, 10):
            print(" " * self.system.screenSizeX)

    def drawGame(self):
        system = self.system
        player = system.player
        store = system.store
        system.Update()
        print((self.cor.GRAY + '██' + self.cor.Color_Off) * self.sizeX)
        for y in range(self.sizeY):
            print((self.cor.GRAY + '██' + self.cor.Color_Off), end = '')
            for x in range(self.sizeX - 2):
                char = "  "
                if system.northEntrance.posX == x and system.northEntrance.posY == y:
                    char = system.northEntrance.character
                if system.southEntrance.posX == x and system.southEntrance.posY == y:
                    char = system.southEntrance.character
                #Mostra os objetos
                for rock in system.rocksInScene:
                    if rock.posX == x and rock.posY == y:
                        char = rock.character
                #Mostra a loja
                if self.system.level == 0:
                    if store.posX == x and store.posY == y:
                        char = store.character
                #Mostra o player
                if player.posX == x and player.posY == y:
                    char = player.character
                 #Mostra o inmigo
                if self.system.enemy.posX == x and self.system.enemy.posY == y:
                    char = self.system.enemy.character
                print(self.cor.BACKGROUND_COLOR + char + self.cor.Color_Off, end='')
            print((self.cor.GRAY + '██' + self.cor.Color_Off))
        print((self.cor.GRAY + '██' + self.cor.Color_Off) * self.sizeX)
        self.gameHUD()

    def drawMenu(self):
        self.system.menuUpdate()
        print('██' * self.sizeX)
        for y in range(self.sizeY):
            print('██', end = '')
            if y == self.sizeY - 22:
                print(self.cor.YELLOW + '       ______  __  __  ______  ______ ______        ' + self.cor.Color_Off + '██')
            elif y == self.sizeY - 21:
                print(self.cor.YELLOW + '      /\  ___\/\ \_\ \/\  __ \/\  ___/\__  _\       ' + self.cor.Color_Off + '██')
            elif y == self.sizeY - 20:
                print(self.cor.YELLOW + '      \ \___  \ \  __ \ \  __ \ \  __\/_/\ \/       ' + self.cor.Color_Off + '██')
            elif y == self.sizeY - 19:
                print(self.cor.YELLOW + '       \/\_____\ \_\ \_\ \_\ \_\ \_\    \ \_\       ' + self.cor.Color_Off + '██')
            elif y == self.sizeY - 18:
                print(self.cor.YELLOW + '        \/_____/\/_/\/_/\/_/\/_/\/_/     \/_/       ' + self.cor.Color_Off + '██')
            elif y == self.sizeY/2 + 3 and self.system.fileManager.hasSaveFile():
                if self.system.menuController.opt == 0:
                    print('   > Continuar o jogo                               ██')
                else:
                    print('    Continuar o jogo                                ██')
            elif y == self.sizeY/2 + 5:
                if self.system.menuController.opt == 1:
                    print('   > Novo jogo                                      ██')
                else:
                    print('    Novo jogo                                       ██')
            elif y == self.sizeY/2 + 7:
                if self.system.menuController.opt == 2:
                    print('   > Highscores                                     ██')
                else:
                    print('    Highscores                                      ██')
            elif y == self.sizeY/2 + 9:
                if self.system.menuController.opt == 3:
                    print('   > Fechar o jogo                                  ██')
                else:
                    print('    Fechar o jogo                                   ██')
            elif y == self.sizeY - 2:
                print('  Ultilize W e S para mover ESPAÇO para selecionar  ██')
            else:
                print('' + ("  " * (self.sizeX - 2) + "██"))
        print('██' * self.sizeX)
        self.hideHUD()

    def drawStore(self):
        system = self.system
        damage = str(self.system.player.pickDamage)
        contPick = str(self.system.contPickaxe)
        self.system.storeUpdate()
        print('██' * self.sizeX)
        for y in range(self.sizeY):
            print('██', end = '')
            if y == self.sizeY - 25:
                print(self.cor.GREEN + '       /$$        /$$$$$$     /$$$$$  /$$$$$$       ' + self.cor.Color_Off + '██')
            elif y == self.sizeY - 24:
                print(self.cor.GREEN + '      | $$       /$$__  $$   |__  $$ /$$__  $$      ' + self.cor.Color_Off + '██')
            elif y == self.sizeY - 23:
                print(self.cor.GREEN + '      | $$      | $$  \ $$      | $$| $$  \ $$      ' + self.cor.Color_Off + '██')
            elif y == self.sizeY - 22:
                print(self.cor.GREEN + '      | $$      | $$  | $$      | $$| $$$$$$$$      ' + self.cor.Color_Off + '██')
            elif y == self.sizeY - 21:
                print(self.cor.GREEN + '      | $$      | $$  | $$ /$$  | $$| $$__  $$      ' + self.cor.Color_Off + '██')
            elif y == self.sizeY - 20:
                print(self.cor.GREEN + '      | $$      | $$  | $$| $$  | $$| $$  | $$      ' + self.cor.Color_Off + '██')
            elif y == self.sizeY - 19:
                print(self.cor.GREEN + '      | $$$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$      ' + self.cor.Color_Off + '██')
            elif y == self.sizeY - 18:
                print(self.cor.GREEN + '      |________/ \______/  \______/ |__/  |__/      ' + self.cor.Color_Off + '██') 
            elif y == self.sizeY/2:
                if self.system.storeController.opt == 0:
                    print('  > Melhorar picareta: R$ ' + damage + ' nivel: ' + contPick + (' ' * (18 - (len(damage) + len(contPick))))  + '██')
                else:
                    print('   Melhorar picareta: R$ ' + damage + ' nivel: ' + contPick + (' ' * (19 - (len(damage) + len(contPick))))  + '██')
            elif y == self.sizeY/2 + 3:
                if self.system.storeController.opt == 1:
                    print('  > Mais sorte: R$ 500 nível: ' + str(self.system.player.luck) + ' (máximo: 5)         ██')
                else:
                    print('   Mais sorte: R$ 500 nível: ' + str(self.system.player.luck) + ' (máximo: 5)          ██')
            elif y == self.sizeY/2 + 6:
                if self.system.storeController.opt == 2:
                    print('  > Dias mais lentos: R$ 100 nível: ' + str(self.system.player.dayDuration + 1) + ' (máximo: 4)   ██')
                else:
                    print('   Dias mais lentos: R$ 100 nível: ' + str(self.system.player.dayDuration + 1) + ' (máximo: 4)    ██')
            elif y == self.sizeY/2 + 9:
                if self.system.storeController.opt == 3:
                    print('  > Sair da loja                                    ██')
                else:
                    print('   Sair da loja                                     ██')
            elif y == self.sizeY - 2:
                print('  Ultilize W e S para mover ESPAÇO para selecionar  ██')
            else:
                print('' + ("  " * (self.sizeX - 2) + "██"))
        print('██' * self.sizeX)
        self.gameHUD()
        

    def drawGameOver(self):
        self.system.gameOverUpdate()
        nick = self.system.nick.upper()
        print('██' * self.sizeX)
        for y in range(self.sizeY):
            print('██', end = '')
            if y == self.sizeY/2-10:
                print('     _____  ______ _____  _____  ______ _    _      ██')
            elif y == self.sizeY/2-9:
                print('    |  __ \|  ____|  __ \|  __ \|  ____| |  | |     ██')
            elif y == self.sizeY/2-8:
                print('    | |__) | |__  | |__) | |  | | |__  | |  | |     ██')
            elif y == self.sizeY/2-7:
                print('    |  ___/|  __| |  _  /| |  | |  __| | |  | |     ██')
            elif y == self.sizeY/2-6:
                print('    | |    | |____| | \ \| |__| | |____| |__| |     ██')
            elif y == self.sizeY/2-5:
                print('    |_|    |______|_|  \_\_____/|______|\____/      ██')
            elif y == self.sizeY/2-2:
                print('               Digite seu nick: ' + nick  + (' ' * (20 - len(nick))) + '██')
            elif y == self.sizeY/2+1 and len(nick) >= 3:
                print('      Muito bem, ' + nick + '! Aqui estão seus dados:        ██')
            elif y == self.sizeY/2+3 and len(nick) >= 3:
                print('      Minérios coletados: ' + str(self.system.minedRocks) + ' ' * (26 - len(str(self.system.minedRocks))) + '██')
            elif y == self.sizeY/2+4 and len(nick) >= 3:
                print('      Dinheiro atual: ' + str(self.system.player.money) + ' ' * (30 - len(str(self.system.player.money))) + '██')
            elif y == self.sizeY/2+5 and len(nick) >= 3:
                print('      Nível da picareta: ' + str(self.system.contPickaxe) + ' ' * (27 - len(str(self.system.contPickaxe))) + '██')
            elif y == self.sizeY/2+7 and len(nick) >= 3:
                print('      Pontuação total: ' + str(self.system.score) + ' ' * (29 - len(str(self.system.score))) + '██')
            elif y == self.sizeY - 2 and len(nick) >= 3:
                print('          Pressione ESPAÇO para continuar           ██')
            else:
                print('' + ("  " * (self.sizeX - 2) + "██"))
        print('██' * self.sizeX)
        self.hideHUD()

    def drawHighscore(self):
        self.system.restartMenu()
        scores = self.system.fileManager.readHighScore()
        first = scores[0].split('-')
        second = scores[1].split('-')
        third = scores[2].split('-')
        print('██' * self.sizeX)
        for y in range(self.sizeY):
            print('██', end = '')
            if y == self.sizeY/2-10:
                print(self.cor.GOLD + '                   .-=========-.                    ██')
            elif y == self.sizeY/2-9:
                print("                   \ -=======- /                    ██")
            elif y == self.sizeY/2-8:
                print('                   _|         |_                    ██')
            elif y == self.sizeY/2-7:
                print('                  ((|         |))                   ██')
            elif y == self.sizeY/2-6:
                print('                   \|         |/                    ██')
            elif y == self.sizeY/2-5:
                print('                    \__     __/                     ██')
            elif y == self.sizeY/2-4:
                print('                      _`) (`_                       ██')
            elif y == self.sizeY/2-3:
                print('                    _/_______\_                     ██')
            elif y == self.sizeY/2-2:
                print('                   /___________\                    ██')
            elif y == self.sizeY/2:
                print("                   1°: " + first[0].upper() + ": " + first[1] + " " * (24 - len(first[1])) +"██")
            elif y == self.sizeY/2 + 2:
                print(self.cor.SILVER +"                   2°: " + second[0].upper() + ": " + second[1] + " " * (24 - len(second[1])) + self.cor.GOLD + "██")
            elif y == self.sizeY/2 + 4:
                print(self.cor.BRONZE +"                   3°: " + third[0].upper() + ": " + third[1] + " " * (24 - len(third[1])) + self.cor.GOLD + "██")
            elif y == self.sizeY - 2:
                print("        Aperte ESPAÇO para voltar ao menu.          ██")
            else:
                print('' + ("  " * (self.sizeX - 2) + "██"))
        print('██' * self.sizeX)
        self.hideHUD()

    def sceneToDraw(self):
        gameState = self.system.gameState
        if gameState == 0:
            self.drawMenu()
        elif gameState == 1:
            self.drawGame()
        elif gameState == 2:
            self.drawGameOver()
        elif gameState == 3:
            self.drawStore()
        elif gameState == 4:
            self.drawHighscore()


#