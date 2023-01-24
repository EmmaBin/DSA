#https://leetcode.com/problems/unique-number-of-occurrences/description/

from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter=defaultdict(int)
        for num in arr:
            counter[num] +=1
        occurrences= set()
        for key, value in counter.items():
            if value in occurrences:
                return False
            occurrences.add(value)

        return True

#Time complexity: O(N)

#We iterate over the array arr to find the frequency 
# and store them in the hash map freq. 
# Then, we insert these frequencies in the hash set freqSet, 
# which has the insertion complexity of O(1). Hence, 
# the total time complexity is equal to O(N).

#Space complexity: O(N).

#We are storing the NNN frequencies in the hash map freq that takes O(1) 
# space for each element. 
# We also store the frequency count in the hash set. Therefore, 
# the total space complexity is equal to O(N)


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        
        # create a hash map
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        if len(set(dic.values())) != len(set(arr)):
            return False
        return True


    d=dict(Counter(arr))
    s=set(d.values())
    
    return len(d.values())==len(s)

