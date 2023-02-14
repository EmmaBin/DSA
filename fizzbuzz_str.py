#Have the function FizzBuzz(num) take the num parameter being passed and return all the numbers from 1 to num separated by spaces, 
# but replace every number that is divisible by 3 with the word "Fizz", 
# replace every number that is divisible by 5 with the word "Buzz", 
# and every number that is divisible by both 3 and 5 with the word "FizzBuzz". 
# For example: if num is 16, then your program should return the string "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16". 
# The input will be within the range 1 - 50.


def FizzBuzz(num):
  result = []
  for i in range(1, num+1):
    if i % 15 ==0:
      result.append('FizzBuzz')
    elif i % 3 ==0:
      result.append('Fizz')
    elif i % 5 ==0:
      result.append('Buzz')
    else:
      result.append(str(i))

  # code goes here
  return ' '.join(result)

# keep this function call here 
print(FizzBuzz(input()))