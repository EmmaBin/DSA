#https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.presum= [0]
        #要注意自己建立的prefix sum是什么样的，比如现在这题可以把index 0 是零，之后的每一个数是前面（i-1）的sum 
        for n in nums:
            self.presum.append(self.presum[-1]+n)
            


        
#with leading 0
    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right+1]-self.presum[left]

#method 2: basic method
class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right + 1):
            sum = sum + self.arr[i]
        return sum