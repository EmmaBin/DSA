#Have the function DivisionStringified(num1,num2) take both parameters being passed, divide num1 by num2, and return the result as a string with properly formatted commas. 
#If an answer is only 3 digits long, return the number with no commas (ie. 2 / 3 should output "1"). 
#For example: if num1 is 123456789 and num2 is 10000 the output should be "12,346".

def DivisionStringified(num1,num2):
  import math

  # code goes here
  return "{:,}".format(math.floor((num1/num2) + .5))

# keep this function call here 
print(DivisionStringified(input()))


def DivisionStringified(num1,num2):

  x = num1 // num2
  y = (num1 / num2) % 1
  
  if y >= 0.5:
    x += 1
  else:
    pass
  
  x = str(x)
  x = x[::-1]

  ans = ''

  for i, c in enumerate(x):
    if i % 3 == 0 and i != 0:
      ans += ',' + c
    else:
      ans += c

  return ans[::-1]  

# keep this function call here 
print(DivisionStringified(input()))