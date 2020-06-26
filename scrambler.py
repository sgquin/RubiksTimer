import random


def scrambler(turns):
    moves = ["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'", "D2", "F", "F'", "F2", "B", "B'", "B2"]
    if turns < 1:
        return ''
    if turns-1 == 0:
        spot = random.randint(0,len(moves)-1)
        return  moves[spot] + scrambler(turns-1)
    spot = random.randint(0,len(moves)-1)
    return moves[spot] + ', ' +scrambler(turns-1)
    
def trScrambler():
    size =  int(input('What size puzzle would you like a scramble for (3-5)? '))
    moves3 = ["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'", "D2", "F", "F'", "F2", "B", "B'", "B2"]
    moves4 = ['R', "R'", "R2", "Rw", "Rw'", "Rw2", "U", "U'", "U2", "Uw", "Uw'", "Uw2", 'F', "F'", "F2", "Fw", "Fw'", "Fw2",'L', "L'", "L2", "Lw", "Lw'", "Lw2",'D', "D'", "D2", "Dw", "Dw'", "Dw2", 'B', "B'", "B2", "Bw", "Bw'", "Bw2", "r", "r'", "r2","u", "u'", "u2", "f", "f'", "f2","l", "l'", "l2", "d", "d'", "d2","b", "b'", "b2"]
    if size == 3:
        return accScrambler(moves3, 25,'X')
    if size == 4:
        return accScrambler(moves4, 25,'X')
    if size == 5:
        return accScrambler(moves4, 25,'X')
 

def accScrambler(moves, turns, scramble):
    spot = random.randint(0,len(moves)-1)
    thisMove = moves[spot]
    if thisMove[0] == scramble[0]:
         return accScrambler(moves,turns, thisMove)
    if turns == 1:
        return thisMove
    return thisMove + ', ' + accScrambler(moves, turns-1,thisMove)
    
    
    
    
    



