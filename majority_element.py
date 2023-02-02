#https://leetcode.com/problems/majority-element/description/

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter  = Counter(nums)
        for key, val in counter.items():
            if val >= (len(nums)/2):
                return key


#A majority element in this case has to appear definitely at the mid of array as the condition says 
# it appears more than n/2 times.
#Sort the list and return the mid element.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]