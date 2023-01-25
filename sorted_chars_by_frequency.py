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




    class Solution:
    def frequencySort(self, s: str) -> str:
        return reduce(lambda a, b: a + b[1]*b[0], Counter(s).most_common(), '')


from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        s1, c = '', Counter(s)
        for k,v in c.most_common():
            s1 = s1 + k*v
        return s1  