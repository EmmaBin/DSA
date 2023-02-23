#Have the function AlphabetSearching(str) take the str parameter being passed and 
# return the string true if every single letter of the English alphabet exists in the string, 
# otherwise return the string false. 
# For example: if str is "zacxyjbbkfgtbhdaielqrm45pnsowtuv" then your program should return the string true 
# because every character in the alphabet exists in this string even though some characters appear more than once.


def AlphabetSearching(strParam):
  new_str= strParam.lower()
  result = ''
  for letter in new_str:
    if letter.isalpha():
      result += letter
  result = set(result)
  if len(result)== 26:
    return True
  else:
    return False

  # code goes here
 

# keep this function call here 
print(AlphabetSearching(input()))


import re

def AlphabetSearching(str):
  str = str.lower()
  chars = set(re.findall('[a-z]', str))

  if len(chars) != 26:
    return 'false'
  else:
    return 'true'

  # code goes here


# keep this function call here 
print(AlphabetSearching(input()))