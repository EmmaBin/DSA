#Have the function LargestPair(num) take the num parameter being passed and determine the largest double digit number within the whole number. 
#For example: if num is 4759472 then your program should return 94 
#because that is the largest double digit number. The input will always contain at least two positive digits.

def LargestPair(num):
  num_str = str(num)
  result = []
  for i in range(len(num_str)-1):
    curr = int(num_str[i] + num_str[i+1])
    result.append(curr)


  # code goes here
  return max(result)

# keep this function call here 
print(LargestPair(input()))

def LargestPair(num):
  num_str = str(num)
  max_num =0
  for i in range(len(num_str)-1):
    curr = int(num_str[i] + num_str[i+1])
    if curr >max_num:
      max_num = curr


  # code goes here
  return max_num

# keep this function call here 
print(LargestPair(input()))

def LargestPair(num):
  to_string = str(num)
  maximum = 0
  for i in range(len(to_string[:-1])):
    number = int(to_string[i:i+2])
    if number > maximum:
      maximum = number
  # code goes here
  return maximum

# keep this function call here 
print(LargestPair(input()))