
#Have the function ElementMerger(arr) take the array of positive integers stored in arr and perform the following algorithm: 
# continuously get the difference of adjacent integers to create a new array of integers, 
# then do the same for the new array until a single number is left and return that number. 
# For example: if arr is [4, 5, 1, 2, 7] then taking the difference of each pair of elements produces the following new array: [1, 4, 1, 5]. 
# Then do the same for this new array to produce [3, 3, 4] -> [0, 1] -> 1. 
# So for this example your program should return the number 1 because that is what's left at the end.
def get_difference(num1, num2):
  return abs(num1-num2)


def ElementMerger(arr):
  if len(arr) ==1:
    return arr[0]
  result = []
    
  for i in range(len(arr)-1):
    result.append(get_difference(arr[i], arr[i+1]))
  return ElementMerger(result)