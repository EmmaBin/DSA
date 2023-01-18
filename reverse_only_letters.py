#https://leetcode.com/problems/reverse-only-letters/description/

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:


        s_list=list(s)
        i=0
        j=len(s)-1

        while j>i:
            if not s_list[i].isalpha():
                i+=1
                #if there is no continue, it won't work, bcz
                #the function of continue here means 
                continue
            if not s_list[j].isalpha():
                j-=1
                continue
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i +=1
            j-=1

        return ''.join(s_list)

#intuitive way
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        result =[]
        #create a list only container the alpha in original order
        only_letter=[char for char in s if char.isalpha()]

        for word in s:
            if word.isalpha():
                #if it's alpha, means this place needs to be replaced with the last word from only_letter
                result.append(only_letter.pop())
            else:
                #if not, I can just place it in the original index number 
                result.append(word)
        return ''.join(result)