import states

def oppositeColor (color):
    if(color == states.States.BLACK):
        return states.States.WHITE
    elif(color == states.States.WHITE):
        return states.States.BLACK
    else:
        print("Fehler in util oppositeColor wurde falsches Argument uebergeben moeglicherweise states.States.FREE")
        return
