#The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . 
# The player must avoid the thunderheads. 
# Determine the minimum number of jumps it will take to jump 
# from the starting postion to the last cloud. 
# It is always possible to win the game.
#Eg. c=[0, 1, 0, 0, 0, 1, 0] return: 3

def jumpingOnClouds(c):
    result = 0
    i = 0
    while i != len(c)-1:
        if i!= len(c)-2 and c[i+2] ==0:
            i+=2
        else:
            i+=1
        result += 1
    return result