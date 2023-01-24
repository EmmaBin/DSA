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


    
    def frequencySort(self, s: str) -> str:
	sCounter = Counter(s)
	result = []
	for key, value in sorted(sCounter.items(), key=lambda x:x[1], reverse=True):
		result.append(key*value)
	return ''.join(result)