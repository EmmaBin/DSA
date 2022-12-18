#https://leetcode.com/problems/number-of-ways-to-split-array/description/


def waysToSplitArray(self, nums: List[int]) -> int:

    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    ans = 0
    #according to the question, right array need at least one element,
    #so the i need to stop at the second last index
    for i in range(len(nums) - 1):
        left_section = prefix[i]
        right_section = prefix[-1] - prefix[i]
        if left_section >= right_section:
            ans += 1

    return ans