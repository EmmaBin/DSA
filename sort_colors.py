#https://leetcode.com/problems/sort-colors/description/?envType=list&envId=xlem03mm
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #in-place means don't saved to a new arr
        #since we know there are only three digits in the arr, we can leverage this fact
        #index will locate the first ocurrence 
        #count how many zeros, ones, and twos. Then place them in the list
        ones = 0
        twos = 0
        zeros = 0
        for i in nums:
            if i == 0:
                zeros += 1
            if i == 1:
                ones += 1
            if i == 2:
                twos += 1
        for i in range(len(nums)):
            if zeros != 0:
                nums[i] = 0
                zeros -= 1
            elif ones != 0:
                nums[i] = 1
                ones -= 1
            else:
                nums[i] = 2
                twos -= 1