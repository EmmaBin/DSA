#https://leetcode.com/problems/valid-palindrome-ii/
#Given a string s, return true 
# if the s can be palindrome after deleting at most one character from it.


def validPalindrome(self, s: str) -> bool:
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            #delete left and then check if the rest is palindrome
            without_left = s[left+1:right+1]
            without_right = s[left:right]
            if without_left == without_left[::-1] or without_right == without_right[::-1]:
                return True
            else:
                return False
        left+=1
        right-=1
    return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left<right:


            if s[left] != s[right]:
                if s[left:right] == s[left:right][::-1] :
                    return True
                if s[left+1:right+1] == s[left+1:right+1][::-1]:
                    return True
                else:
                    return False
            else:
                left+=1
                right -=1

        return True
    #reverse a string [::-1]
    #s[left+1; right+1] pay attention, to right +1 meaning include right
    #s[left: right] meaning not including right, stop at right-1

    #可以刪去一個，也可以不刪， 如果不用刪，直接往里走，都一樣就是true
    #如果有一個不要的，刪去一個不一樣的剩下的是，也是true，if 裏面有一個true就可以了