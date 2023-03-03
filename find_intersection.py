#Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements:
# the first element will represent a list of comma-separated numbers sorted in ascending order, 
#the second element will represent a second list of comma-separated numbers (also sorted). 
#Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr 
#in sorted order. If there is no intersection, return the string false.

def FindIntersection(strArr):
  result =''
  arr1=strArr[0].split(', ')
  arr2 = strArr[1].split(', ')
  for i in arr1:
    if i in arr2:
      result +=str(i)+','
  if len(result)==0:
    return False

  return result[:-1]
# keep this function call here 
print(FindIntersection(input()))


def FindIntersection(strArr):
  
    setOne = set(strArr[0].split(", "))
    setTwo = set(strArr[1].split(", "))

    result = sorted(list(setOne.intersection(setTwo)), key=lambda x: int(x))
    
    return ','.join(result) if len(result) > 0 else False

# keep this function call here 
print(FindIntersection(input()))