#Have the function RemoveBrackets(str) take the str parameter being passed, 
# which will contain only the characters "(" and ")", 
# and determine the minimum number of brackets that need to be removed to create a string of correctly matched brackets. 
# For example: if str is "(()))" then your program should return the number 1. The answer could potentially be 0, 
# and there will always be at least one set of matching brackets in the string.

def RemoveBrackets(str):
  rep = '()'
  while rep in str:
    str = str.replace(rep,'')
  
  return len(str)

print(RemoveBrackets(input()))


def RemoveBrackets(str):
  count = 0
  ans = 0
  for c in str:
    if c=='(':
      count += 1
    else:
      if count==0:
        ans += 1
      else:
        count += -1
  ans += count
  return ans

def RemoveBrackets(str): 

    # code goes here 
    stack = list()
    for i in str:
      if len(stack) == 0:
        stack.append(i)
      else:
        if i == ')' and stack[-1] == '(':
          stack.pop()
        else:
          stack.append(i)
    return len(stack)