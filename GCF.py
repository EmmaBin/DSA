#Have the function GCF(arr) take the array of numbers stored in arr which will always contain only two positive integers, 
# and return the greatest common factor of them. For example: if arr is [45, 12] then your program should return 3. 
# There will always be two elements in the array and they will be positive integers.

def GCF(arr):

  # code goes here
  largestComFact = 1
  for i in range(2,min(arr)+1):
    if arr[0]%i==0 and arr[1]%i==0:
      largestComFact = i
  return largestComFact

# keep this function call here 
print(GCF(input()))