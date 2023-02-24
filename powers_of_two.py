#Have the function PowersofTwo(num) take the num parameter being passed which will be an integer and return the string true if it's a power of two. 
# If it's not return the string false. 
# For example if the input is 16 then your program should return the string true but if the input is 22 then the output should be the string false.

def PowersofTwo(num):
  for i in range(num):
    if 2**i == num:
      return 'true'
    else:
      return 'false'
#这是我第一次的答案，这样不可行是因为，i只走了一次，如果不等于就是错的了，没有去尝试其他的数字 if else 

def PowersofTwo(num):
  for i in range(num):
     
    if 2**i == num:
      return 'true'
    if 2**i > num:
      return 'false'
print(PowersofTwo(input()))

#这是可行的，因为还有机会一直尝试，如果已经比要得到的答案大了，那肯定就是不对的了


def PowersofTwo(num):
  num = float(num)
  while num > 2:
    num = num/2
  if num == 2: 
    return "true"
  else: 
    return "false"
  # code goes here

# keep this function call here 
print(PowersofTwo(input()))

# / 这个除号得到的是小数形式，而且2.0==2. 