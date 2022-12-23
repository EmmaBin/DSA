#https://leetcode.com/problems/count-number-of-nice-subarrays/

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

#this method is slower
from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        new_nums =[0] * len(nums)
        for i in range (len(nums)):
            if nums[i] % 2 ==0:
                new_nums[i] = 0
            else:
                new_nums[i] = 1

        counts = defaultdict(int)
        counts[0] = 1
        ans = curr =0

        for num in new_nums:
            curr += num
            ans += counts[curr -k]
            counts[curr] +=1
        return ans

#this method is better
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0
        
        for num in nums:
            curr += num % 2
            ans += counts[curr - k]
            counts[curr] += 1

        return ans