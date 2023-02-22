#Have the function OneDecremented(str) count how many times a digit appears that is exactly one less than the previous digit. 
# For example: if str is "5655984" then your program should return 2 because 5 appears directly after 6 and 8 appears directly after 9. 
# The input will always contain at least 1 digit.

def OneDecremented(strParam):
  count = 0
  for i in range(len(strParam) -1):
    if int(strParam[i+1])- int(strParam[i]) == -1:
      count +=1



  # code goes here
  return count

# keep this function call here 
print(OneDecremented(input()))