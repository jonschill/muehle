# coding: utf8
import node
import states

#Bei erzeugung einens Game(s) werden alle für Spiel benoetigten Knoten erzeugt und richtig initialisiert
#außerdem werden sie alle der Liste nodes angehängt
#erst werden alle aeußeren, dann mittleren, dann inneren Knoten angehängt
class Game:
    def __init__(self):
        self.blackStones = 0
        self.whiteStones = 0
        self.nodes = []
        o1 = node.Node("o1", ["o8", "o2"], states.States.FREE)
        self.nodes.append(o1)
        o2 = node.Node("o2", ["o1", "o3", "m2"], states.States.FREE)    
        self.nodes.append(o2)
        o3 = node.Node("o3", ["o2", "o4"], states.States.FREE)
        self.nodes.append(o3)
        o4 = node.Node("o4", ["o3", "o5", "m4"], states.States.FREE)
        self.nodes.append(o4)
        o5 = node.Node("o5", ["o4", "o6"], states.States.FREE)
        self.nodes.append(o5)
        o6 = node.Node("o6", ["o5", "o7", "m6"], states.States.FREE)
        self.nodes.append(o6)
        o7 = node.Node("o7", ["o6", "o8"], states.States.FREE)
        self.nodes.append(o7)
        o8 = node.Node("o8", ["o1", "o7", "m8"], states.States.FREE)
        self.nodes.append(o8)
        
        m1 = node.Node("m1", ["m8", "m2"], states.States.FREE)
        self.nodes.append(m1)
        m2 = node.Node("m2", ["o2", "m1", "m3", "i2"], states.States.FREE)
        self.nodes.append(m2)
        m3 = node.Node("m3", ["m2", "m4"], states.States.FREE)
        self.nodes.append(m3)
        m4 = node.Node("m4", ["o4", "m3", "m5", "i4"], states.States.FREE)
        self.nodes.append(m4)
        m5 = node.Node("m5", ["m4", "m6"], states.States.FREE)
        self.nodes.append(m5)
        m6 = node.Node("m6", ["o6", "m5", "m7", "i6"], states.States.FREE)
        self.nodes.append(m6)
        m7 = node.Node("m7", ["m6", "m8"], states.States.FREE)
        self.nodes.append(m7)
        m8 = node.Node("m8", ["o8", "m1", "m7", "i8"], states.States.FREE)
        self.nodes.append(m8)
        
        
        i1 = node.Node("i1", ["i8", "i2"], states.States.FREE)
        self.nodes.append(i1)
        i2 = node.Node("i2", ["m2","i1", "i3"], states.States.FREE)
        self.nodes.append(i2)
        i3 = node.Node("i3", ["i2", "i4"], states.States.FREE)
        self.nodes.append(i3)
        i4 = node.Node("i4", ["m4", "i3", "i5"], states.States.FREE)
        self.nodes.append(i4)
        i5 = node.Node("i5", ["i4", "i6"], states.States.FREE)
        self.nodes.append(i5)
        i6 = node.Node("i6", ["m6", "i5", "i7"], states.States.FREE)
        self.nodes.append(i6)
        i7 = node.Node("i7", ["i6", "i8"], states.States.FREE)
        self.nodes.append(i7)
        i8 = node.Node("i8", ["m8", "i1", "i7"], states.States.FREE)
        self.nodes.append(i8)
        
        #deklarieren der zusammengehörigen Knoten die eine Mühle bilden könnten
        #nummerierung folgendermaßen: erst die außenlinien der Ringe (außen, mitte, innen(in der Reihenfloge))
        #mit der oberen linie angefangen im Uhrzeigersinn weiter. Danach die linien zwischen den Ringen
        #angefangen auf 12 Uhr im Uhrzeigersinn
        
        self.millLines = []
        
        self.millLines.append([o1, o2, o3])
        self.millLines.append([o3, o4, o5])
        self.millLines.append([o5, o6, o7])
        self.millLines.append([o7, o8, o1])
        
        self.millLines.append([m1, m2, m3])
        self.millLines.append([m3, m4, m5])
        self.millLines.append([m5, m6, m7])
        self.millLines.append([m7, m8, m1])
        
        self.millLines.append([i1, i2, i3])
        self.millLines.append([i3, i4, i5])
        self.millLines.append([i5, i6, i7])
        self.millLines.append([m7, m8, m1])
        
        self.millLines.append([o2, m2, i2])
        self.millLines.append([o4, m4, i4])
        self.millLines.append([o6, m6, i6])
        self.millLines.append([o8, m8, i8])
        
        
        