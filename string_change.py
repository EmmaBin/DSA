#Have the function StringChanges(str) take the str parameter being passed, 
# which will be a string containing letters from the alphabet, 
# and return a new string based on the following rules. Whenever a capital M is encountered, 
# duplicate the previous character (then remove the M), 
# and whenever a capital N is encountered remove the next character from the string (then remove the N).
#  All other characters in the string will be lowercase letters. 
# For example: "abcNdgM" should return "abcgg". The final string will never be empty.


def StringChanges(strParam):
  new_lst = list(strParam)
  if new_lst[0] == 'M':
    new_lst[0] = ''

  if new_lst[-1] == 'N':
    new_lst[-1] = ''
  for i in range(1, len(new_lst)):
    if new_lst[i] == 'M':
      new_lst[i] = new_lst[i-1]

    if new_lst[i] == 'N':
      new_lst[i] = ''
      new_lst[i+1]=''
  return ''.join(new_lst)


#为什么要从range (1) 开始呢？
# https://coderbyte.com/editor/String%20Changes:Python3
