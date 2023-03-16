
#https://leetcode.com/problems/search-insert-position/description/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while right>=left:
            mid = (left + right)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
                
        return left
    

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
   
        i = 0
        j = len(nums) - 1
        while(i <= j):
            pivot = (i + j) // 2
            if (nums[pivot] == target):
                return pivot
            elif (nums[pivot] > target):
                j = pivot - 1
            else:
                i = pivot + 1
        return i