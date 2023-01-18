#https://leetcode.com/problems/minimum-size-subarray-sum/description/
#the order of a few line of codes can totally get different result
#pay attention to the detailed order

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left =0
        curr_sum =0
        result = float('inf')
        right = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                result = min(result, right-left+1)
               
                curr_sum -= nums[left]
                left +=1
            
            

        if result == float('inf'):
            return 0
        else:
            return result