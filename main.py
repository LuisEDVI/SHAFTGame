import os
import cursor
import WConio2 as WConio2
from Screen import *

class main:

    os.system("cls")

    screen = Screen()

    while True:
        cursor.hide()
        WConio2.gotoxy(0,0)  
        screen.sceneToDraw()

    