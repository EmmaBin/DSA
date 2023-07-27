#https://leetcode.com/problems/plus-one/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1
                return digits
        return [1]+digits
    
#The main way that something is returned from the function is the first return statement. 
#In the case where the entire list contains 9s, that return statement is never reached.
#The result should be the original digits array all turned to 0s, with a 1 at the front