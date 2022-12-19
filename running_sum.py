#https://leetcode.com/problems/running-sum-of-1d-array/description/


def runningSum(self, nums: List[int]) -> List[int]:
    prefix_sum=[nums[0]]
    for i in range(1, len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[-1])
        
    return prefix_sum