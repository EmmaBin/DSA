# Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

# Implement the Solution class:

# Solution(int[] nums) Initializes the object with the array nums.
# int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.


from collections import defaultdict
# {number:[index1, index2]}


class Solution:
    # O(n) and O(n)
    def __init__(self, nums: List[int]):
        self.dict = defaultdict(list)
        for i in range(len(nums)):
            self.dict[nums[i]].append(i)

    # O(1) and 0(1)

    def pick(self, target: int) -> int:
        if len(self.dict[target]) == 1:
            return self.dict[target][0]
        else:
            return random.choice(self.dict[target])
