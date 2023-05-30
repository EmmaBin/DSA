#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #constant space
        #each number used only once
        #return in ascending order
        #1-indexed, starts at 1 instead of 0
        #exactly one solution, length is always 2
        # two pointers, equal to target, not equal 
        left = 0
        right = len(numbers)-1
        while right>left:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -=1
            else:
                left +=1