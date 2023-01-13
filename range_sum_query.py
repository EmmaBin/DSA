#https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.presum= [nums[0]]
        for n in nums:
            self.presum.append(self.presum[-1]+n)
            


        

    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right+1]-self.presum[left]
