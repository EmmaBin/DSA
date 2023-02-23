#https://leetcode.com/problems/isomorphic-strings/description/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t={}
        t_to_s={}
        for i in range(len(s)):
            if s[i] not in s_to_t:
                s_to_t[s[i]] = t[i]
            else: 
                if s_to_t[s[i]] != t[i]:
                    return False
                else:
                    continue
        for j in range(len(t)):
            if t[j] not in t_to_s:
                t_to_s[t[j]] = s[j]
            else:
                if t_to_s[t[j]] != s[j]:
                    return False
                else:
                    continue
        return True


#建立两个dictionary,如果能互相map,就是真的，不一样就是假的