#https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i