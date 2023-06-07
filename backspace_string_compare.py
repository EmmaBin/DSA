#https://leetcode.com/problems/backspace-string-compare/description/

#对于last in first out,都要想到stack

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack=[]
        t_stack=[]
        for char in s:
            if char!= '#':
                s_stack.append(char)
            #check if it's a empty list, if empty, don't need to pop
            elif s_stack:
                s_stack.pop()
        for char in t:
            if char!= '#':
                t_stack.append(char)
            elif t_stack:
                t_stack.pop()
        return s_stack == t_stack


#method 2: 既然要写两次，就直接在里面再写一个function
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            stack = []
            for c in s:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()

            return "".join(stack)

        return build(s) == build(t)
    

#6/7 update: if the first char is #, it will throw error, so needed to check this situation

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_backspaced = []
        t_backspaced = []
        
        for i in range(len(s)):
            if s[i] == '#':
                if s_backspaced:
                    s_backspaced.pop()
            else:
                s_backspaced.append(s[i])
            
        for i in range(len(t)):
            if t[i] == '#':
                if t_backspaced:
                    t_backspaced.pop()
            else:
                t_backspaced.append(t[i])
        
        return s_backspaced == t_backspaced