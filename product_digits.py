#Have the function ProductDigits(num) take the num parameter being passed which will be a positive integer, 
#and determine the least amount of digits you need to multiply to produce it. 
#For example: if num is 24 then you can multiply 8 by 3 which produces 24, 
#so your program should return 2 because there is a total of only 2 digits that are needed. 
#Another example: if num is 90, you can multiply 10 * 9, so in this case your program should output 3 
#because you cannot reach 90 without using a total of 3 digits in your multiplication.

def ProductDigits(num):
  i=1
  result=[]
  while i < num/2+1:
    if num % i ==0:
      length = len(str(i))+len(str(num//i))
      result.append(length)
    i+=1
  return min(result)


# keep this function call here 
print(ProductDigits(input()))

#这道题里面，我想涵盖1和数字本身作为factor是关键，并且，要考虑遇到input是1的话，while condition用到的是 / 而不是 //， /会得到小数，
#第二点，每一次update是应该在if 外面，如果在if里面就不能每一次都update