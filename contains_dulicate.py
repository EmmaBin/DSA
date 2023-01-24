#https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_nums = set(nums)
        if len(new_nums)== len(nums):
            return False
        else:
            return True

from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for n in nums:
            count[n] +=1

        for key, value in count.items():
            if value >1:
                return True
        
        return False


#  We start off by sorting the given array. 
#  Once we loop through the array from the beginning, 
#  if we see that the current number is the same as the next one in the array, 
#  there contains a duplicate in the array and therefore we return true. 
#  If we finish looping and there are no duplicates, we return false.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #一定要先sort，把一样大小的放一起，相邻的数字有一样就可以return了
        nums.sort()
        left = 0
        right = left+1
        while right<len(nums):
            if nums[left] == nums[right]:
                return True
            left+=1
            right+=1
        return False