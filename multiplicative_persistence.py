#Have the function MultiplicativePersistence(num) take the num parameter being passed which will always be a positive integer 
#and return its multiplicative persistence which is the number of times you must multiply the digits in num until you reach a single digit. 
#For example: if num is 39 then your program should return 3 because 3 * 9 = 27 then 2 * 7 = 14 and finally 1 * 4 = 4 and you stop at 4.

def MultiplicativePersistence(num):
  num_str= str(num)
  count = 0
  while len(num_str)>1:
    product = 1
    for ele in num_str:
      product *= int(ele)
    num_str = str(product)
    count +=1

  # code goes here
  return count

# keep this function call here 
print(MultiplicativePersistence(input()))