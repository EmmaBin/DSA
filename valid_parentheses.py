#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        match = {')':'(', '}':'{', ']':'[' }

        for char in s:
            if char in match:
                if stack and stack[-1] == match[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if not stack :
            return True
        else:
            return False


#O(n) and O(n), bcz using hash takes up O(n) space