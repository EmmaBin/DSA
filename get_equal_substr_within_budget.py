#https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        curr = ans = left = 0  

        for right in range(len(s)):
            curr += abs((ord(t[right]) - ord(s[right])))

            #while the condition is not meeting our requirement which is less or equal to maxCost,
            #we need to update the sum of this subarray by subtracting the left indexing and advance the left pointer
            #until the condition met, exit the while loop, keep hold of that length 
            while curr > maxCost:
                curr -= abs((ord(t[left]) - ord(s[left])))
                left += 1 
            
            ans = max(ans, right - left + 1)
        
        return ans 


#method 2
class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        
        start = 0
        ans = 0
        cur = 0
        
        for end in range(len(s)):
            
            val = abs(ord(s[end]) - ord(t[end]))
            cur += val
            if cur <= maxCost:
                ans = max(ans, end-start+1)
            else:
                while cur > maxCost:
                    cur -= abs(ord(s[start]) - ord(t[start]))
                    start += 1
                
        return ans