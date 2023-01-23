#https://leetcode.com/problems/sum-of-unique-elements/description/


# TC:
# SC:
from collections import defaultdict
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        #create a dictionary: key-> number, value-> occurrence
        # only take the key: 1, sum(key)
        counter = defaultdict(int)
        for n in nums:
            counter[n] +=1
        result = 0
        for key in counter:
            if counter[key] ==1:
                result += key
        return result




class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = {}
        for x in nums: freq[x] = 1 + freq.get(x, 0)
        return sum(x for x in nums if freq[x] == 1)