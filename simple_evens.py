#Have the function SimpleEvens(num) check whether every single number in the passed in parameter is even. 
#If so, return the string true, otherwise return the string false. 
#For example: if num is 4602225 your program should return the string false because 5 is not an even number.

def SimpleEvens(num):
  num =str(num)
  for n in num:
    if int(n) % 2 !=0:
      return False

  # code goes here
  return True

# keep this function call here 
print(SimpleEvens(input()))

#integer is not iterable, that's just a number, need to convert to str or any type of iterable