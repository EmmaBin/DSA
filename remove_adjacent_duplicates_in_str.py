#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            else:
                if stack[-1] == char:
                    stack.pop()
                else:
                    stack.append(char)
        return ''.join(stack)

# o(n) o(n)
#''.join(list_name), 前面的delimiter 用什么来间隔，只有list都是str,才能这么用
