#Have the function NonrepeatingCharacter(str) take the str parameter being passed, 
#which will contain only alphabetic characters and spaces, 
#and return the first non-repeating character. 
#For example: if str is "agettkgaeee" then your program should return k. 
#The string will always contain at least one character and there will always be at least one non-repeating character.

def NonrepeatingCharacter(s):
  for i in range(len(s)):
    if s[i].isalpha():
      if s[i] not in s[i+1:] and s[i] not in s[:i]:
        return s[i]

  # code goes here

# keep this function call here 
print(NonrepeatingCharacter(input()))

#除了loop到那之后，后面也没有并且前面也没有才是unique


def NonrepeatingCharacter(str):
  rtn = 0
  for l in str:
    if str.count(l) < 2:
      return l
# keep this function call here 
print(NonrepeatingCharacter(input()))

def NonrepeatingCharacter(input_str):
  input_str = input_str.lower()
  chars_dict = {}

  for char in range(len(input_str)):
    if input_str[char] in chars_dict:
      chars_dict[input_str[char]] += 1
    else:
      chars_dict[input_str[char]] = 1
  
  for key, value in chars_dict.items():
    if value == 1:
      return key

# keep this function call here 
print(NonrepeatingCharacter(input()))