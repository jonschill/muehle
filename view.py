# coding: utf8
import node
import states
import game
#wandelt den eingegebenen node abhaengig von seinem Zustand in die Zeichen o, *, # um
def fillNode(n):
    if(n.state == "free"):
        return "o"
    if(n.state == "black"):
        return "*"
    if(n.state == "white"):
        return "#"
    #Ausnahmefall. Exception?
    else:
        return "?"
    
#fragt fuer jeden node den Zustand ab und fuegt das entsprechende Zeichen in den Spielfeld String ein
def printField(g):
    field = "" + fillNode(g.nodes[0]) + "--------"
    field += fillNode(g.nodes[1]) + "--------"
    field += fillNode(g.nodes[2]) + "\n|        |        |\n|   "
    
    field += fillNode(g.nodes[8]) + "----"
    field += fillNode(g.nodes[9]) + "----"
    field += fillNode(g.nodes[10]) + "   |\n|   |    |    |   |\n|   | "
    
    field += fillNode(g.nodes[16]) + "--"
    field += fillNode(g.nodes[17]) + "--"
    field += fillNode(g.nodes[18]) + " |   |\n|   | |     | |   |\n"
    
    
    field += fillNode(g.nodes[7]) + "---"
    field += fillNode(g.nodes[15]) + "-"
    field += fillNode(g.nodes[23]) + "     "
    
    field += fillNode(g.nodes[19]) + "-"
    field += fillNode(g.nodes[11]) + "---"
    field += fillNode(g.nodes[3]) + "\n|   | |     | |   |\n|   | "
    
    
    field += fillNode(g.nodes[22]) + "--"
    field += fillNode(g.nodes[21]) + "--"
    field += fillNode(g.nodes[20]) + " |   |\n|   |    |    |   |\n|   "
    
    field += fillNode(g.nodes[14]) + "----"
    field += fillNode(g.nodes[13]) + "----"
    field += fillNode(g.nodes[12]) + "   |\n|        |        |\n"
    
    field += fillNode(g.nodes[4]) + "--------"
    field += fillNode(g.nodes[5]) + "--------"
    field += fillNode(g.nodes[6]) + "\n"
    
    print(field)