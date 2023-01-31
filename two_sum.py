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