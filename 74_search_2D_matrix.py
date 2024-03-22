#https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0]) #长
        n = len(matrix) #宽
        left = 0
        right = m*n-1
        while left <= right:
            mid = (left+right) //2
            mid_row, mid_col = divmod(mid, m)
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] > target:
                right = mid -1
            else:
                left = mid+1
        return False