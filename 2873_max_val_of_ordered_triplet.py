class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        l = len(nums)
        diff = [0]*l
        curr_max = nums[0]
        for i in range(1, l-1):
            if curr_max - nums[i] > diff[i-1]:
                diff[i] = curr_max - nums[i]
            else:
                diff[i] = diff[i-1]

            if nums[i] > curr_max:
                curr_max = nums[i]

        for j in range(l-1, 1, -1):

            total = nums[j] * diff[j-1]
            result = max(result, total)
        return result
