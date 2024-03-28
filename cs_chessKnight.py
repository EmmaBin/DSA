# Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

# The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.


def solution(cell):
    r = 0
    c = [ord(cell[0])-96,int(cell[1])]
    
    m = [[1,2],[2,1],[1,-2],[-2,1],[-1,2],[2,-1],[-1,-2],[-2,-1]]
    
    for i in m:
        if 0<c[0]+i[0]<9 and 0<c[1]+i[1]<9:
            r +=1
    return r  