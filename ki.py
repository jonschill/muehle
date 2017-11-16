import states
import game
import util
#prueft ob die uebergebene Farbe fast eine Muehle hat
#also zwei Steine der gleichen Farbe auf einer Linie liegen
#die dritte position in der Reihe kann aber von einem gegnerischen Stein belegt haben
def hasPotentialMill1(color, g):
    millCounter = 0
    for i in range(len(g.millLines)):
        tokenCounter = 0
        for j in range(len(g.millLines[i])):
            if(g.millLines[i][j].state == util.oppositeColor(color)):
                tokenCounter += 1
        if(tokenCounter == 2):
            millCounter += 1
    return millCounter

#prueft ob die uebergebene Farbe fast eine Muehle hat
#also zwei Steine der gleichen Farbe auf einer Linie liegen
#die dritte postion muss frei sein
def hasPotentialMill2(color, g):
    millCounter = 0
    for i in range(len(g.millLines)):
        tokenCounter = 0
        for j in range(len(g.millLines[i])):
            if(g.millLines[i][j].state == color):
                tokenCounter += 1
            if(g.millLines[i][j].state == color):
                tokenCounter -= 1
        if(tokenCounter == 2):
            millCounter += 1
    return millCounter

#prueft ob die uebergebene Farbe in ihrem naechsten Zug eine muehle haben koennte
#also on hasPotentialMill2 gilt und ein Stein der Farbe neben dem freien Feld liegt
def hasMillInNextDraw(color, g):
    