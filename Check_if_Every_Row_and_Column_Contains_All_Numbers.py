#https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/description/

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        #n==len(matrix)
        #check each row => subarr, each col=>same index from each subarr
        #falsy conditon => turn into set, lengh of set != n
        #num inside the set <1, >n
        #return true in the end
        #有什么办法不用nested loop, improve time complexity 吗
        n = len(matrix)
        new_set= set()
        for i in range(n):
            for j in range(n):
                new_set.add(matrix[i][j])
            print(new_set)
            if len(new_set) != n:
                return False
            for num in new_set:
                if num <1 or num > n:
                    return False
            new_set=set()
        
        another_set = set()
        #(0,0)(1,0)(2,0)
        for i in range(n):
            for j in range(n):
                another_set.add(matrix[j][i])
            if len(another_set) != n:
                return False
            for num in another_set:
                if num <1 or num > n:
                    return False
            another_set=set()
        return True
    
#我自己通过debug改了两次做对， 一次是在每一个set之后都要check,checked condition should be
#inside the loop,一次是,每一次check 之后都要变成empty在做