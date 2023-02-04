#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

#这道题的关键是如果用下面的two pointers，要想什么时候advance pointers, 当右面的指针
#所指的数字因为一样被pop之后，其实指针就已经自动指向新的一个数字了，所以无需再　advance任何指针，
#接着进行compare就可以了
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        right=1
        while right < len(nums):
            if nums[left] == nums[right]:
                nums.pop(right)
 
            else:
                left+=1
                right+=1


def removeDuplicates(self, nums: List[int]) -> int:
    slow, fast = 0, 1
    while fast in range(len(nums)):
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            nums[slow+1] = nums[fast]
            fast += 1
            slow += 1

    return slow + 1

def removeDuplicates(self, nums: List[int]) -> int:
    j = 0
    for i in range(1, len(nums)):
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]
    return j + 1
