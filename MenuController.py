import WConio2 as WConio2

class Controller:

    hasSelected = False

    def __init__(self, starterOpt, numberOfOpts, isStore):
        self.starterOpt = starterOpt
        self.opt = starterOpt
        self.opts = numberOfOpts
        if(isStore):
            self.isStore = isStore
            self.closedStore = False

    def playerSelection(self): 
        if WConio2.kbhit():
            (key, symbol) = WConio2.getch()
            if symbol == 'w':
                self.opt -= 1
                if self.opt < self.starterOpt:
                    self.opt = self.opts
            if symbol == 's':
                self.opt += 1
                if self.opt > self.opts:
                    self.opt = self.starterOpt
            if symbol == " ":
                self.hasSelected = True
            if symbol == "p" and self.isStore:
                self.closedStore = True