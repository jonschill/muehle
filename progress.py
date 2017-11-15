# coding: utf8
import game
import states
import view
import actions
import re

#Steine werden am Anfang des Spiels abwechselnd gesetzt
def setStones(g):
    while(g.blackStones < 3 and g.whiteStones < 3):
        setStone(states.States.BLACK, g)
        setStone(states.States.WHITE, g)

#Das setzen eines Steines mit der Farbe color
def setStone(color, g):
    colorString = colorToString(color)
    
    draw = raw_input(colorString + ': setze einen Stein: ') 
    while(actions.set(draw, color, g) == False):
        print("Ungültige Eingabe")
        draw = raw_input(colorString + ': setze einen Stein: ') 
    view.printField(g)
    
    
def moveStones(g):
    while(g.blackStones > 1 and g.whiteStones > 1):
        moveStone(states.States.BLACK, g)
        #gibt es durch den Zug eine mülhle und muss in der Folge 1 Stein entfernt werden?
        mills = hasMill(states.States.BLACK, g)
        if(mills > 0):
            removeStones(mills, states.States.WHITE, g)
        
        moveStone(states.States.WHITE, g)
        #gibt es durch den Zug eine mülhle und muss in der Folge 1 Stein entfernt werden?
        mills = hasMill(states.States.WHITE, g)
        if(mills > 0):
            removeStones(mills, states.States.BLACK, g)
        
#bewege einen Stein
def moveStone(color, g):
    colorString = colorToString(color)
    
    draw = raw_input(colorString + ': bewege einen Stein: ')
    drawList = re.split(':', draw)
    while(len(drawList) != 2):
        print("Zu viele oder zu wenige Parameter")
        draw = raw_input(colorString + ': bewege einen Stein: ')
        drawList = re.split(':', draw)
    while(actions.move(drawList[0], drawList[1], color, g) == False):
        print("Ungültige Eingabe")
        draw = raw_input(colorString + ': bewege einen Stein: ')
        drawList = re.split(':', draw)
        while(len(drawList) != 2):
            print("Zu viele oder zu wenige Parameter")
            draw = raw_input(colorString + ': bewege einen Stein: ')
            drawList = re.split(':', draw)
    view.printField(g)
    
#n-viele steine der Farbe color entfernen
def removeStones(n, color, g):
    colorString = colorToString(color)
    for i in range(n):
            draw = raw_input('entferne einen Stein von ' + colorString+ ': ') 
            while(actions.remove(draw, color, g) == False):
                print("Ungültige Eingabe")
                draw = raw_input('entferne einen Stein von ' + colorString+ ': ')
            view.printField(g)
    
#prüft ob die übergebene Farbe eine Mühle hat
def hasMill(color, g):
    millCounter = 0
    for i in range(len(g.millLines)):
        if(g.millLines[i][0].state == color and g.millLines[i][1].state == color and g.millLines[i][2].state == color):
            millCounter += 1
    return millCounter

#übergebene Farbe wird als String ausgegeben
def colorToString(color):
    if(color == states.States.BLACK):
        colorString = "Schwarz"
    if(color == states.States.WHITE):
        colorString = "Weiß"
    else:
        #Exception schmeißen!!!
        print("Fehler. Argument ist keine gültige Farbe")
        return
    return colorString
            

g = game.Game()
setStones(g)
moveStones(g)