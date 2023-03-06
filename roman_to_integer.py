#https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        #"MCMXCIV"
        look_up={'I':1, 'V':5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000 }
        total = 0
        for i in range(len(s)-1):
            if look_up[s[i]]<look_up[s[i+1]]:
                total -= look_up[s[i]]
            else:
                total += look_up[s[i]]
        total += look_up[s[-1]]
        return total