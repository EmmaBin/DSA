#Array Addition I
#Have the function ArrayAdditionI(arr) take the array of numbers stored in arr and return the string true if any combination of numbers in the array (excluding the largest number) can be added up to equal the largest number in the array, 
# otherwise return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true because 4 + 6 + 10 + 3 = 23. The array will not be empty, 
# will not contain all the same elements, 
# and may contain negative numbers

#Input: [3,5,-1,8,12]
#Output: true

import itertools


def ArrayAdditionI(arr):

  # code goes here
  the_num = max(arr)
  arr.remove(s)
  comb = []
  for i in range(len(arr) + 1):
    #itertools.combinations return tuples, i is the length
    #for each length, it generates all the possible combinations
    for tupl in itertools.combinations(arr, i):
      comb.append(sum(tupl))
  for x in comb:
    if x == the_num:
      return 'true'
  return 'false'
 
print(ArrayAdditionI(input()))