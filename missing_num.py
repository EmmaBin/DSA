#https://leetcode.com/problems/missing-number/description/

#time complexity will be O(n)
def missingNumber(self, nums: List[int]) -> int:
    new_set = set(nums)
    for i in range(len(nums)+1):
        if i not in new_set:
            return i


#no extra way used here, a Math problem, find the sum difference 
def missingNumber(self, nums: List[int]) -> int:
    new_sum=0
    for i in range(len(nums)+1):
        new_sum += i
    old_sum=0

    for i in range(len(nums)):
        old_sum += nums[i]
    return (new_sum - old_sum)

