#Have the function NumberAddition(str) take the str parameter, 
# search for all the numbers in the string, add them together, 
# then return that final number. For example: if str is "88Hello 3World!" the output should be 91. 
# You will have to differentiate between single digit numbers and multiple digit numbers like in the example above. 
# So "55Hello" and "5Hello 5" should return two different answers. 
# Each string will contain at least one letter or symbol.

import re
def NumberAddition(strParam):
  number_list = re.split('[^0-9]', strParam)
  total=0
  for number in number_list:
    if number:
      total += int(number)

  

  # code goes here
  return total

# keep this function call here 
print(NumberAddition(input()))
#using regex to split the string into list, delimiter is non-numerical element
#loop over the list to add up the number, str=>int

def NumberAddition(str):
  num = ''
  for i in str:
    if i.isnumeric():
      num += i
    else:
      num += ' '
  num = num.split()
  num = [int(i) for i in num]
  return sum(num)

# keep this function call here 
print(NumberAddition(input()))