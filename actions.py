# coding: utf-8
import node
import states
import game
#gibt, falls existierend, den node zurueck der die Postition hat, die mit dem uebergebenen String uebereinstimmt
def getNodeByName(pos, gm):
    for n in gm.nodes:
        if (n.position == pos):
            return n
        
def move(oldPos, newPos, color, g):
    try:
        oldNode = getNodeByName(oldPos, g)
        newNode = getNodeByName(newPos, g)
        if(oldNode.state == color and oldNode.isNeighbor(newPos) and newNode.state == states.States.FREE):
            newNode.state = oldNode.state
            oldNode.state = states.States.FREE
            return True
        else:
            return False
    except AttributeError:
        return False
        
def set(pos, color, g):
    try:
        node = getNodeByName(pos, g)
        if(node.state == states.States.FREE):
            node.state = color
            if(color == states.States.BLACK):
                g.blackStones +=1
            if(color == states.States.WHITE):
                g.whiteStones +=1
            return True
        else:
            return False
    except AttributeError:
        return False

def remove(pos, color, g):
    node = getNodeByName(pos, g)
    try:
        if(node.state == states.States.BLACK and color == states.States.BLACK):
            g.blackStones -=1
            node.state = states.States.FREE
            return True
        if(node.state == states.States.WHITE and color == states.States.WHITE):
            g.whiteStones -=1
            node.state = states.States.FREE
            return True
        return False
    except AttributeError:
        return False
    