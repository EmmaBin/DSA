
#https://leetcode.com/problems/path-crossing/description/


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        #how to represent path crossing in letters
        #use set to store corordinate pairs, if there is duplicates meaning crossing
        cor = {'N': [0,1], 'E': [1,0], 'S': [0,-1], 'W': [-1,0]}
        #create an empty set
        result_set=set()
        result_set.add((0,0))
        x, y = 0, 0
        for direction in path:
            x += cor[direction][0]
            y += cor[direction][1]
            if (x,y) not in result_set:
                #when adding new tuple, here is double()
                result_set.add((x,y))
            else: 
                return True
        return False