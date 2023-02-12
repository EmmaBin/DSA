#Have the function SnakeCase(str) take the str parameter being passed and 
#return it in proper snake case format where each word is lowercased and separated from adjacent words via an underscore. 
#The string will only contain letters and some combination of delimiter punctuation characters separating each word.

#For example: if str is "BOB loves-coding" then your program should return the string bob_loves_coding.


import re
def SnakeCase(strParam):
  lower_case = strParam.lower()
  lower_lst = re.split('[^a-z]', lower_case)
  return '_'.join(lower_lst)


  # code goes here


# keep this function call here 
print(SnakeCase(input()))


def SnakeCase(str):
  for char in str:
    if not char.isalpha(): str = str.replace(char, '_')
  return str.lower()

# keep this function call here 
print(SnakeCase(input()))
