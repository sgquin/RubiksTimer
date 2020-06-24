import random


def scrambler(turns):
    moves = ["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'", "D2", "F", "F'", "F2", "B", "B'", "B2"]
    if turns < 1:
        return ''
    if turns-1 == 0:
        spot = random.randint(0,len(moves)-1)
        return moves[spot] + scrambler(turns-1)
    spot = random.randint(0,len(moves)-1)
    return moves[spot] + ', ' +scrambler(turns-1)

def trScrambler(turns):
    return accScrambler(turns,'X')

def accScrambler(turns, scramble):
    moves = ["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'", "D2", "F", "F'", "F2", "B", "B'", "B2"]
    spot = random.randint(0,len(moves)-1)
    thisMove = moves[spot]
    if thisMove[0] == scramble[0]:
         return accScrambler(turns, thisMove)
    if turns == 1:
        return thisMove
    return thisMove + ', ' + accScrambler(turns-1,thisMove)
    
    
    
    
    



