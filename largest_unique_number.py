#https://leetcode.com/problems/largest-unique-number/

from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        possible_num =[]
        for key in counts:
            if counts[key] == 1:
                possible_num.append(key)
        if len(possible_num) >0:
            return max(possible_num)
        else:
            return -1