#Have the function TwoSum(arr) take the array of integers stored in arr, 
# and determine if any two numbers (excluding the first element) in the array can sum up to the first element in the array. 
# For example: if arr is [7, 3, 5, 2, -4, 8, 11], then there are actually two pairs that sum to the number 7: [5, 2] and [-4, 11]. 
# Your program should return all pairs, with the numbers separated by a comma, in the order the first number appears in the array. 
# Pairs should be separated by a space. 
# So for the example above, your program would return: 5,2 -4,11

#If there are no two numbers that sum to the first element in the array, return -1

def TwoSum(arr):

  res = []
  s = arr[0]
  for i in range(1, len(arr)-1):
    x = arr[i]
    for j in range(i+1, len(arr)):
      if x + arr[j] == s:
        res.append(str(x)+","+str(arr[j]))
  if len(res) > 0:
    return " ".join(res)
  else:
    return "-1"
print(TwoSum(input()))



def TwoSum(arr):

  pairs = []
  
  total = arr[0]
  arr = arr[1:]

  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if arr[i] + arr[j] is total:
        pairs.append([arr[i], arr[j]])

  
  if len(pairs) is 0:
    return -1
  return ' '.join(map(lambda x: f"{x[0]},{x[1]}", pairs))