#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_lst =[]
        max_len = 0
        #loop over the str and save each char in the new_list, 
        #if there is any duplicates, check the length without the duplicate
        #save the max_len, update it everytime and return the max value
        #how to update the max value, using max method, update the len of each list

        for char in s:
            if char in new_lst:
                new_lst = new_lst[new_lst.index(char)+1:]
            new_lst.append(char)
           
            max_len = max(max_len, len(new_lst))
        return max_len

from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res