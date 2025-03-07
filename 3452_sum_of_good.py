class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        for i in range(len(nums)):
            if i-k >= 0:
                if nums[i] <= nums[i-k]:
                    continue
            if i+k < n:
                if nums[i] <= nums[i+k]:
                    continue
            total += nums[i]
        return total
