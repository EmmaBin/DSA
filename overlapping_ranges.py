#Have the function OverlappingRanges(arr) take the array of numbers stored in arr which will contain 5 positive integers,
# the first two representing a range of numbers (a to b), the next 2 also representing another range of integers (c to d), and a final 5th element (x) which will also be a positive integer, 
#and return the string true if both sets of ranges overlap by at least x numbers. For example: if arr is [4, 10, 2, 6, 3] then your program should return the string true. 
#The first range of numbers are 4, 5, 6, 7, 8, 9, 10 and the second range of numbers are 2, 3, 4, 5, 6. The last element in the array is 3, and there are 3 numbers that overlap between both ranges: 4, 5, and 6. 
#If both ranges do not overlap by at least x numbers, then your program should return the string false.


def OverlappingRanges(arr):
  list1=[]
  list2=[]
  for i in range(arr[0], arr[1]+1):
    list1.append(i)
  for j in range(arr[2], arr[3]+1):
    list2.append(j)
  total_len= len(list1+list2)
  result = total_len - len(set(list1+list2))
  

  if result >= arr[-1]:
    return 'true'
  else:
    return 'false'


  # code goes here
  

# keep this function call here 
print(OverlappingRanges(input()))
#这道题我用了十五分钟，很开心，在遇到关卡的时候，我还能坚持想别的办法接着做，及时调整，及时改错，即使可能心里慌慌的我
#还是接着做，我想这些也是面试官想看到的，想找的。
#找到两个overlap的数字有几个 是这个问题的关键




def OverlappingRanges(arr):
  first_set = set(range(arr[0],arr[1]+1))
  second_set = set(range(arr[2],arr[3]+1))
  if len(first_set.intersection(second_set)) >= arr[4]:
    return 'true'
  return 'false'

# keep this function call here 
print(OverlappingRanges(input()))