#Have the function ClosestEnemyII(strArr) read the matrix of numbers stored in strArr which will be a 2D matrix 
#that contains only the integers 1, 0, or 2. Then from the position in the matrix where a 1 is, 
#return the number of spaces either left, right, down, or up you must move to reach an enemy 
#which is represented by a 2. You are able to wrap around one side of the matrix to the other as well. 
#For example: if strArr is ["0000", "1000", "0002", "0002"] then this looks like the following:

0 0 0 0
1 0 0 0
0 0 0 2
0 0 0 2

#For this input your program should return 2 because the closest enemy (2) is 2 spaces away from the 1 
#by moving left to wrap to the other side and then moving down once. 
# The array will contain any number of 0's and 2's, but only a single 1. 
# It may not contain any 2's at all as well, where in that case your program should return a 0.

def ClosestEnemyII(strArr):
  # parse strArr
  grid = [[int(x) for x in y] for y in strArr]
  # get dimensions of array
  height, width = len(grid), len(grid[0])
  # find the 1
  for i in range(height):
    for j in range(width):
      if grid[i][j] == 1:
        (x, y) = (i, j)
        break
  # scan for 2's; keep track of minimum distance
  dist = height + width + 2
  for i in range(height):
    for j in range(width):
      if grid[i][j] == 2:
        new_dist = min(abs(x - i), width - abs(x - i)) + min(abs(y - j), height - abs(y - j))
        dist = min(dist, new_dist)
  if dist < height + width + 2:
    return dist
  return 0

# keep this function call here 
print(ClosestEnemyII(input()))