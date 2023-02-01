#https://leetcode.com/problems/pascals-triangle/

#Time complexity: O(numRows2)
#Space complexity: O(1)
#o see why, consider how many overall loop iterations there are. 
# The outer loop obviously runs numRowsnum times, 
# but for each iteration of the outer loop, the inner loop runs rowNum times. 


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [0]*numRows
        for i in range(numRows):
            #每一次都要重建一个新的subarr
            lst[i] = [0]* (i+1)
            lst[i][0]=1
            lst[i][i]=1#第一行有一个，第二行有两个，最后一个是1
            for j in range(1,i):
                #掐头去尾
                lst[i][j] = lst[i-1][j-1]+lst[i-1][j]
        return lst
