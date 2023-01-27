
#https://leetcode.com/problems/permutation-in-string/description/
#O(n^2) 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_string = ''.join(sorted(s1))
        current_string = ''
        for char in s2:
            current_string += char
            if len(current_string) == len(target_string):
                if ''.join(sorted(current_string)) == target_string:
                    return True
                current_string = current_string[1:]
        return False


from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = Counter(s1)
        for i in range(len(s2)-len(s1)+1):
            s2_sub_dict=Counter(s2[i:i+len(s1)])
            if s1_dict == s2_sub_dict:
                return True
            s2_sub_dict ={}
        return False


from collections import defaultdict
def a_fun(s1, s2):
  s1_dic = defaultdict(int)
  for char in s1:
    s1_dic[char] +=1
  print(s1_dic)

  for i in range(len(s2)-len(s1)+1):
    s2_dic= defaultdict(int)
    for char in s2[i:i+len(s1)]:
      s2_dic[char]+=1
    
    if s1_dic == s2_dic:
      return True
    
  return False