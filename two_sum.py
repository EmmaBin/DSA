#https://leetcode.com/problems/two-sum/description/
#to optimize this question. I can use dictionary to increase time complexity to O(n)
#space complexity to O(n)


def twoSum(self, nums: List[int], target: int) -> List[int]:
    lookup_dict={}
    for index, num in enumerate(nums):
        difference= target - num
        if difference in lookup_dict:
            return[index, lookup_dict[difference]]
        lookup_dict[num] = index

#dictionary is very useful for quick lookup, instead of looping twice, using dictionary
#will only loop once


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result =[]
        for idx in range(len(nums)):
            if target - nums[idx] in nums and idx != nums.index(target-nums[idx]):
                result.append(idx)
        return result
    

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            num1 = nums[i]
            num2 = target - num1
            
            # Check if the complement exists in the remaining part of the list
            if num2 in nums[i+1:]:
                # Return the indices of the two numbers that add up to the target
                return [i, nums.index(num2, i+1)]
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i
#O(n**2)


