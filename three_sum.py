

#Have the function ThreeSum(arr) take the array of integers stored in arr, 
# and determine if any three distinct numbers (excluding the first element) in the array can sum up to the first element in the array. 
# For example: if arr is [8, 2, 1, 4, 10, 5, -1, -1] then there are actually three sets of triplets that sum to the number 
# 8: [2, 1, 5], [4, 5, -1] and [10, -1, -1]. Your program should return the string true if 3 distinct elements sum to the first element,
#  otherwise your program should return the string false. The input array will always contain at least 4 elements.

#O(n^2)
import itertools
def ThreeSum(arr):
  the_num = arr[0]
  arr.remove(arr[0])
  for tupl in itertools.combinations(arr,3):
    if sum(tupl) == the_num:
      return True

  # code goes here
  return False

def ThreeSum(arr):
  total = arr.pop(0)
  l = len(arr)
  for i1 in range(l - 2):
    for i2 in range(i1 + 1, l - 1):
      if total - arr[i1] - arr[i2] in arr[i2 + 1: l]:
        return 'true'
  return 'false'

# keep this function call here 
print(ThreeSum(input()))