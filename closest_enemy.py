#Have the function ClosestEnemy(arr) take the array of numbers stored in arr and from the position in the array 
#where a 1 is, return the number of spaces either left or right you must move to reach an enemy 
#which is represented by a 2. 
#For example: if arr is [0, 0, 1, 0, 0, 2, 0, 2] then your program should return 3 
#because the closest enemy (2) is 3 spaces away from the 1. The array will contain any number of 0's and 2's, but only a single 1. 
#It may not contain any 2's at all as well, where in that case your program should return a 0.

def ClosestEnemy(arr):
  #case1, no 2
  if 2 not in arr:
    return 0
  #case2, 1 is on the left side of 2
  if arr.index(1) < arr.index(2):
    return arr.index(2) - arr.index(1)
  #case3, 2 is on the left side
  i_position = arr.index(1)

  for j in range(i_position, -1, -1):

    if arr[j]==2:
      
      return i_position-j

  # code goes here

# keep this function call here 
print(ClosestEnemy(input()))