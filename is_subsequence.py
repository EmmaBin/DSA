#https://leetcode.com/problems/is-subsequence/

def isSubsequence(self, s: str, t: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i]==t[j]:
            i+=1
            j+=1
        else: 
            j+=1
    if i == len(s):
        return True
    else:
        return False


#if i can loop over to the end of the s, meaning letters in s found hall its matches