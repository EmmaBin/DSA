#https://leetcode.com/problems/max-consecutive-ones-iii/


def longestOnes(self, nums: List[int], k: int) -> int:


    start = 0
    res = float('-inf')

    zero_count = 0

    for end in range(len(nums)):

        if nums[end] == 0 :

            zero_count += 1
        # when zero count is greater than k then shrink the sliding window

        while zero_count > k :
            if nums[start] == 0 :
                zero_count -= 1
            start += 1

        res = max(res, end - start + 1)
    return res