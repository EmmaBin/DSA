#https://leetcode.com/problems/reverse-prefix-of-word/description/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        #based on this hint "first occurrence of ch (inclusive)", use index() method
        #Python index() is an inbuilt function in Python, which searches for a given element from the start of the list and returns the index of the first occurrence. 
        #clarification: 
        #1 uppercase lowercase, both are lower cases
        #2 if not found, return the original word
        #3, inclusive
        #highlevel:
        # get the index() first, two pointers (left=0, right= index)
        # only traverse the segment and reverse the str
        if ch not in word:
            return word
        #since str is not mutable, convert to list first
        word_list = list(word)
        target = word_list.index(ch)
        #since it's inclusive
        left=0
        right=target
        #remember to set the condition, and advance pointers
        while right >left:
            word_list[left], word_list[right] = word_list[right], word_list[left]
            left+=1
            right-=1
        return ''.join(word_list)