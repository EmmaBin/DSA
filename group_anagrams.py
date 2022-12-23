#https://leetcode.com/problems/group-anagrams/

#method 1 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = {}
        if len(strs)<1:
            return strs
        else:
            
            for i in range(len(strs)):
                reg = strs[i]
                sorted_word = "".join(sorted(reg))
                if sorted_word not in solution:
                    solution[sorted_word] = [reg]
                else:
                    solution[sorted_word].append(reg)
                
        return solution.values()
        #dictionary.values() doesn't actually return a list, 
        #but actually a view object. However, 
        #the LeetCode judge accepts it as a valid format.


#method 2 similar to method 1
#using sorted list as key

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        
        return groups.values()

#notes:
#'eat' ==> sorted('eat') ==> ['a', 'e', 't']
#['a', 'e', 't'] ==> "".join(['a', 'e', 't']) ==> 'aet'
#sorted把string變list
#"".join()把list變string

#Given n as the length of strs and m as the average length of the strings,
#we iterate over each string sort it, which costs O(n * m * log m). 
#Then, we need to iterate over the keys. 
#In the worst case scenario, when there are no matching anagrams, there will be n groups, 
#which means this will cost O(n), 
#giving an overall time complexity of O(n⋅m⋅logm) (the final + n is dominated).
#The space complexity is O(n⋅m) as each string will be placed in an array within the hash map.