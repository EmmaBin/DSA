class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        if x == 0:
            return 0

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid-1
            else:
                left = left+1
        return right
# what worth noticing is the last right pointer holds the last valid value that satisfies  mid * mid <= x when the loop ends
# in comparison with 35, it returns left
