
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
        # 1. get the prefix sum arr
        # 2. build a dictionary and initiate a cnt variable
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


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #prefix sum 
        #prefix_sum arr[index] - prefix_sum[another_index] = goal 
        prefix_sum=[0]*len(nums)
        prefix_sum[0]= nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = nums[i]+ prefix_sum[i-1]

        prefix_dict ={}
        result = 0
        for num in prefix_sum:
            if num == goal:
                result +=1
            if num-goal in prefix_dict:
                result += prefix_dict[num-goal]
            if num not in prefix_dict:
                prefix_dict[num] = 1
            # if num in prefix_dict: 如果这样写的话就是错的
            #if use counter or defualtdict to construct the dictionary first, not working either
            else：
                prefix_dict[num] +=1

        return result