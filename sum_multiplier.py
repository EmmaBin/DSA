#Have the function SumMultiplier(arr) take the array of numbers stored in arr and 
#return the string true if any two numbers can be multiplied so that the answer is greater than double the sum of all the elements 
#in the array. If not, return the string false. For example: if arr is [2, 5, 6, -6, 16, 2, 3, 6, 5, 3] 
#then the sum of all these elements is 42 and doubling it is 84. 
#There are two elements in the array, 16 * 6 = 96 and 96 is greater than 84, 
#so your program should return the string true.

import itertools
def SumMultiplier(arr):
  target = sum(arr)*2
  for pair in list(itertools.combinations(arr,2)):
    if pair[0]*pair[1] > target:
      return True

  # code goes here
  return False

# keep this function call here 
print(SumMultiplier(input()))


def SumMultiplier(arr):
  target = sum(arr) * 2

  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if arr[i] * arr[j] > target:
        return 'true'
  # code goes here
  return 'false'

# keep this function call here 
print(SumMultiplier(input()))