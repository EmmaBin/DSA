#https://leetcode.com/problems/jewels-and-stones/description/

from collections import defaultdict
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counts = defaultdict(int)
        ans= 0
        for letter in stones:
            counts[letter] += 1
        for char in jewels:
            ans += counts[char]
        return ans