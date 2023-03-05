#Have the function MovingMedian(arr) read the array of numbers stored in arr which will contain a sliding window size,
# N, as the first element in the array and the rest will be a list of numbers. 
#Your program should return the Moving Median for each element based on the element and its N-1 predecessors,
# where N is the sliding window size. 
#The final output should be a string with the moving median corresponding to each entry in the original array separated by commas.

#Note that for the first few elements (until the window size is reached), 
#the median is computed on a smaller number of entries. For example: if arr is [3, 1, 3, 5, 10, 6, 4, 3, 1] then your program should output "1,2,3,5,6,6,4,3"
import statistics

def MovingMedian(arr):

  WindowSize = arr[0]
  Data = arr[1:]
  N = len(Data)
  retArr = []

  for i in range(N):
    if (i < WindowSize):
      window = Data[0:i+1]
      
    else:
      window = Data[(i-WindowSize)+1:i+1]

    window.sort()
    retArr.append(str(round(statistics.median(window))))
    

  
  # code goes here
  return ','.join(retArr)

# keep this function call here 
print(MovingMedian(input()))


from statistics import median

def MovingMedian(arr):
  n = arr.pop(0)
  w = n - 1
  mids = []
  for i in range(len(arr)):
    if i <= w:
      mids.append(int(median(arr[:i+1])))
    else:
      mids.append(int(median(arr[i-w:i+1])))
  # code goes here
  return ','.join(list(map(str, mids)))

# keep this function call here 
print(MovingMedian(input()))