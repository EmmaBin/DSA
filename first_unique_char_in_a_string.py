#https://leetcode.com/problems/first-unique-character-in-a-string/description/

#注意 str.index(letter)也可以用于string
#return第一个符合条件的就可以

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        look_up = Counter(s)
        for key, value in look_up.items():
            if value == 1:
                return s.index(key)
        return -1