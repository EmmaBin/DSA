#Have the function AdditivePersistence(num) take the num parameter being passed which will always be a positive integer
# and return its additive persistence which is the number of times you must add the digits in num 
#until you reach a single digit.
#For example: if num is 2718 then your program should return 2 
#because 2 + 7 + 1 + 8 = 18 and 1 + 8 = 9 and you stop at 9.

def AdditivePersistence(num):
  num_str = str(num)
  count =0
  while len(num_str)>1:
    total =0
    for i in num_str:
      total += int(i)
    num_str = str(total)
    count +=1
  return count


#这道题的重点有三个：
    #1. 不要把input int 复杂化，转化成str就可以有 len 和 iterate 的属性了
    #2. 在whileloop里面我才需要设置 total =0, 这样每一次才能从头得到一个新的数字
    #3. 这个数字就是需要我再次计算它的长度的，所以重新assign name到 num_str, 这样我才能一直给新的数据传送过去到while condition 里面




def AdditivePersistence(num, counter=0):
  if len(str(num)) == 1:
    return counter
  
  sum = 0
  for s in list(str(num)):
    sum += int(s)
  return AdditivePersistence(sum, counter + 1)

# keep this function call here 
print(AdditivePersistence(input()))