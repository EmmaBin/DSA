# Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

# The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:


def solution(bishop, pawn):
    ord1= ord(bishop[0])
    ord2= ord(pawn[0])
    return abs(ord1-ord2) == abs(int(bishop[1])- int(pawn[1]))


#此题重点在于会画辅助线，能在斜线上，就是说明两点的长和宽一样长