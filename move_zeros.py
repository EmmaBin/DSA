#https://leetcode.com/problems/move-zeroes/description/

#two pointers method: switch 0 and none-zeros, switch everytime, make sure 0 always stay behind

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] !=0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1


#second method:
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #initiate two pointers
        left = 0
        #i will keep moving evertime,but left pointer will conditionally advance, it's job is to locate the 0s
        for i in range(len(nums)):
            if nums[left] ==0:
                del nums[left]
                nums.append(0)
            else:
                left+=1
#third method:
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #initiate two pointers
        left = 0
        right = len(nums)-1

        while left<right:
            if nums[left] ==0:
                del nums[left]
                nums.append(0)
                right -=1
            else:
                left+=1

