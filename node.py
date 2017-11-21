# coding: utf8
import states
#repraesentiert einen Knoten auf dem Spielfeld
#Die Attribute sind: seine Position auf dem Spielfeld:
#-o steht dabei für den aeußeren Ring, m für den mittleren, i für den inneren
#-die Nummern identifizieren einen Knoten innerhalb seines Rings. Die Nummerierung faengt oben links an
#Eine Liste mit den Postitionen seiner Nachbarn
#Seinen Zustand: frei/von schwarz/weiß belegt
class Node: 
    def __init__(self, p, n, s):
        self.position = p
        self.neighbors = n
        self.state = s
    #gibt an ob uebergebene Knoten (candidat) ein Nachbar der Instanz ist   
    def isNeighbor(self, candidat):
        for n in self.neighbors[:]:
            if(n == candidat):
                return True
        return False
            