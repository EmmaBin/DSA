#https://leetcode.com/problems/reverse-only-letters/description/

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:


        s_list=list(s)
        i=0
        j=len(s)-1

        while j>i:
            if not s_list[i].isalpha():
                i+=1
                continue
            if not s_list[j].isalpha():
                j-=1
                continue
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i +=1
            j-=1

        return ''.join(s_list)
