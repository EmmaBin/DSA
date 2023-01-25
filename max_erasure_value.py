
#https://leetcode.com/problems/maximum-erasure-value/
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        result = total = 0
        left  = 0
        seen =set()
        for right in range(len(nums)):
            # adjust the left bound of sliding window until you get all unique elements
            while left < right and nums[right] in seen:
                seen.remove(nums[left])
                total -= nums[left]
                left+=1
            
            
            total += nums[right]
            seen.add(nums[right])
            result = max(result, total)
        return result
# Time - O(n)
# Space - O(k) - where k is number of unique elements in input nums.



