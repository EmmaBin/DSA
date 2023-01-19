#https://leetcode.com/problems/find-pivot-index/description/


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # detailed logic:
        # 1. get prefic_sum array
        # 2. based on this array to form a new list of tuples
        # 3. in each tuple (new_list[curr]-nums[curr], new_list[-1]-new_list[curr])
        
      
        # O(n) and O(n)
        if len(nums) == 0: return -1
        dp = [0] * len(nums)
        dp[0] = nums[0]
        #following step is creating a prefix_sum
        for i in range(1, len(nums)):
            dp[i] = dp[i - 1] + nums[i]
        #using each sum to compare
        for i in range(len(nums)):
            if dp[i] - nums[i] == dp[-1] - dp[i]:
                return i
        return -1

        # second thought:
        # get the sum of the whole list, set left sum as 0
        # and then loop over the list, while looping over, subtract the current value from the sum, and add it to the left sum, if found a match, return that index

        list_sum= sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            list_sum -= nums[i]
            if list_sum == left_sum:
                return i
            left_sum += nums[i]

        return -1