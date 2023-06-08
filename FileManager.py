import os

class File:

    def __init__(self):
        self.hasSave = self.hasSaveFile()
        
    def hasSaveFile(self):
        return os.path.isfile("savefile.txt")

    def saveGame(self, highestLevel, money, pickDamage, dayDuration, day, contPick, minedRocks, luck):
        savefile = open('savefile.txt', 'w')
        savefile.write(str(highestLevel) + '.' + str(money) + '.' + str(pickDamage) + '.' + str(dayDuration) + '.' + str(day) + '.' + str(contPick) + '.' + str(minedRocks) + '.' + str(luck))
        savefile.close
        
    def readSave(self):
        savefile = open('savefile.txt', 'r')
        save = savefile.read().split('.')
        savefile.close()
        return save
    
    def deleteSave(self):
        if self.hasSaveFile:
            os.remove("savefile.txt")

    def createHighScores(self):
        if not os.path.isfile("highscores.txt"):
            highscores = open("highscores.txt", 'w')
            highscores.write("N/A-0.N/A-0.N/A-0")
            highscores.close()

    def setHighScore(self, index, name, score):
        highscores = open("highscores.txt", 'r')
        scores = highscores.read().split('.')
        highscores.close()
        playerHighscore = str(name) + '-' + str(score)
        if index == 0:
            first = scores[0]
            second = scores[1]
            scores[0] = playerHighscore
            scores[1] = first
            scores[2] = second
        elif index == 1:
            second = scores[1]
            scores[1] = playerHighscore
            scores[2] = second
        elif index == 2:
            scores[2] = playerHighscore
        highscores = open("highscores.txt", 'w')
        highscores.write('.'.join(scores))
        highscores.close()

    def readHighScore(self):
        highscores = open("highscores.txt", 'r')
        scores = highscores.read().split('.')
        highscores.close()
        return scores

