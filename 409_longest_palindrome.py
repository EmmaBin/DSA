#https://leetcode.com/problems/longest-palindrome/description/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        l=len(s)
        s_set=set()
        for letter in s:
            if letter not in s_set:
                s_set.add(letter)
            else:
                s_set.remove(letter)
        set_length=len(s_set)
        if set_length != 0:
            return  l- set_length + 1
        else:
            return l