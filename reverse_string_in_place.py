#Write a function that reverses a string. 
# The input string is given as an array of characters s.

#You must do this by modifying the input array in-place with O(1) extra memory.
#Do not return anything, modify s in-place instead.


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left=0
        right = len(s)-1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right]= temp
            left +=1
            right -=1


#pay attention to the requirement: in-place
#two pointer starts at both ends, and iterate towards the middle, 
#switch the elements each time,
#use a temp to hold the current value which will be assigned later

#? is this align with the O(1) extra memory requirement??