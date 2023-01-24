#https://leetcode.com/problems/sort-characters-by-frequency/description/

from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        #大小写不一样
        result=''
        counter=defaultdict(int)
        for letter in s:
            counter[letter] +=1
            
        char_sorted = sorted(counter, key=counter.get, reverse = True)
        for char in char_sorted:
            result +=(char*counter[char])
        return result