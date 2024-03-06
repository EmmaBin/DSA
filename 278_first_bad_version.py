#https://leetcode.com/problems/first-bad-version/description/

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low=1
        high=n
        find_answer = False
        while find_answer != True:
            middle = (low+high)//2
            if isBadVersion(middle) and not isBadVersion(middle-1):
                return middle
            elif isBadVersion(middle):
                high=middle-1
            elif not isBadVersion(middle):
                low=middle+1