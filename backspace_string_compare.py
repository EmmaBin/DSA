# https://leetcode.com/problems/backspace-string-compare/description/

# 对于last in first out,都要想到stack

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for char in s:
            if char != '#':
                s_stack.append(char)
            # check if it's a empty list, if empty, don't need to pop
            elif s_stack:
                s_stack.pop()
        for char in t:
            if char != '#':
                t_stack.append(char)
            elif t_stack:
                t_stack.pop()
        return s_stack == t_stack


# method 2: 既然要写两次，就直接在里面再写一个function
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


# 6/7 update: if the first char is #, it will throw error, so needed to check this situation

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

    class Solution:

    def backspaceCompare(self, s: str, t: str) -> bool:
        # helper func to get next valid string

        def helper(st, index):
            backspace = 0
            while index >= 0:
                if st[index] == "#":
                    index -= 1
                    backspace += 1
                elif backspace > 0:
                    backspace -= 1
                    index -= 1
                elif st[index] != "#" and backspace == 0:
                    break

            return index

        p1 = len(s)-1
        p2 = len(t)-1

        while p1 >= 0 or p2 >= 0:
            p1 = helper(s, p1)
            p2 = helper(t, p2)

            if p1 >= 0 and p2 >= 0 and s[p1] != t[p2]:
                return False

            if (p1 < 0) != (p2 < 0):
                return False
            p1 -= 1
            p2 -= 1

        return True
