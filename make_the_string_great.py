#https://leetcode.com/problems/make-the-string-great/

#method 1 iteration O(n*n) O(n)
class Solution:
    def makeGood(self, s: str) -> str:
        # if s has less than 2 characters, we just return itself.
        while len(s) > 1:
            # 'find' records if we find any pair to remove.
            find = False
            
            # Check every two adjacent characters, curr_char and next_char.
            for i in range(len(s) - 1):
                curr_char, next_char = s[i], s[i + 1]
                
                # If they make a pair, remove them from 's' and let 'find = True'.
                if abs(ord(curr_char) - ord(next_char)) == 32:
                    s = s[:i] + s[i + 2:]
                    find = True
                    break
            
            # If we cannot find any pair to remove, break the loop. 
            if not find:
                break
        return s

#method 2 stack O(n) O(n)

class Solution:
    def makeGood(self, s: str) -> str:
        # Use stack to store the visited characters.
        stack = []
        
        # Iterate over 's'.
        for curr_char in list(s):
            # If the current character make a pair with the last character in the stack,
            # remove both of them. Otherwise, we add the current character to stack.
            if stack and abs(ord(curr_char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(curr_char)
        
        # Returns the string concatenated by all characters left in the stack.
        return "".join(stack)


#Key takeaway for me was ascii('a') - ascii('A') is always 32 (Since it is 97 - 65)

#此题重点是找到一个方法证明相邻的两个，一个是大写一个是小写