#https://leetcode.com/problems/simplify-path/description/

class Solution:
    def simplifyPath(self, path: str) -> str:
        #convert to a list use '/' as delimeter
        path_list = path.split('/')
        #get rid of empty string from the list
        path_list = [a for a in path_list if a !='']

        stack=[]
        for char in path_list:
            if char =='.':
                continue
            #double dots meaning delete the last element in the list
            elif char == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return '/' + '/'.join(stack)