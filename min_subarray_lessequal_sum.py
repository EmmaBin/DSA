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
                #result should be checked first
                #这时候，left还在满足条件的位置，每一个满足条件的位置都应该被记下来
                #所以 update result 要在while loop 里面，而且是第一个应该被check
                #如果左边，移动了一位，还满足条件，再被check
                result = min(result, right-left+1)
               
                curr_sum -= nums[left]
                left +=1
            
            

        if result == float('inf'):
            return 0
        else:
            return result