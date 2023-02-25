#Have the function OffLineMinimum(strArr) take the strArr parameter being passed which will be an array of integers ranging from 1...n and the letter "E" and return the correct subset based on the following rules. 
#The input will be in the following format: ["I","I","E","I",...,"E",...,"I"] 
#where the I's stand for integers and the E means take out the smallest integer currently in the whole set. 
#When finished, your program should return that new set with integers separated by commas. For example: if strArr is ["5","4","6","E","1","7","E","E","3","2"] then your program should return 4,1,5.


def OffLineMinimum(strArr):
  num_arr=[]
  result =[]
  for i in strArr:
    if i !='E':
      num_arr.append(i)
    else:
      num_arr.sort()
      result.append(num_arr.pop(0))
  # code goes here
  return ','.join(result)

# keep this function call here 
print(OffLineMinimum(input()))
#space complexity is O(n)
#这个问题起初 我想的是fast slow pointers, 可是当两个E连着出现时，就会出现空arr, 也是在于我没有完全理解题的意思
#把字母当成一个信号，碰到这个信号就找出现在以后所有的subarr里面最小的即可，分开两个arr是最有效的，并且注意 loop时候
#是loop index 还是里面的每一天字母
