
#https://leetcode.com/problems/binary-subarrays-with-sum/description/


#If we found that arr[idx]-goal exists in our hashmap, 
#we update the counter cnt += dic[arr[idx]-goal]:

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        arr = [0] * n
        arr[0] = nums[0]
        for idx in range(1, n):
            arr[idx] = arr[idx-1] + nums[idx]
        dic = {}
        cnt = 0
        for idx, val in enumerate(arr):
            if val == goal:
                cnt += 1
            if val - goal in dic:
                cnt += dic[val-goal]
            if val not in dic:
                dic[val] = 1
            else:
                dic[val] += 1
        return cnt
