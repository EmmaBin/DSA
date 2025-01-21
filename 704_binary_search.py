class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # method 2: recursion
        def helper(low, high, target):
            if low > high:
                return -1
            middle = (low+high)//2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                return helper(middle+1, high, target)
            else:
                return helper(low, middle-1, target)

        return helper(0, len(nums)-1, target)

        # find the value of the middle one
        # compare that value with target
        # target is smaller -> locate left side then repeat
        # target is larger -> locate right side then repeat

        # left = 0
        # right = len(nums)-1

        # while left <= right:#if edge case is [5], and target is 5, we need to let left==right
        #     middle = (left+right)//2
        #     print(middle)
        #     if target == nums[middle]:
        #         return middle
        #     elif target > nums[middle]:
        #         left = middle +1
        #     else:
        #         right = middle -1
        # return -1
