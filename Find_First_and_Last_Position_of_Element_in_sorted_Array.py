# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def search(x):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid+1
                else:
                    hi = mid
            return lo

        lo = search(target)
        hi = search(target+1)-1

        if lo <= hi:
            return [lo, hi]

        return [-1, -1]


# two pointer - O(n)

    class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = 0
        right = len(nums) - 1
        # mid is target: starting, middle, ending
        # mid is not a target num
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return check_duplicates(mid, target, nums)

        return [-1, -1]

# [1] 1


def check_duplicates(index, target, nums):
    start = index
    end = index

    while start >= 0 and nums[start] == target:
        start -= 1
    start = start+1

    while end < len(nums) and nums[end] == target:
        end += 1
    end = end-1

    return [start, end]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def searchFirst(nums, target):
            first = -1
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] == target:
                    first = mid
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid+1
            return first

        def searchLast(nums, target):
            last = -1
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] == target:
                    last = mid
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid+1
            return last

        first = searchFirst(nums, target)
        last = searchLast(nums, target)
        return [first, last]
