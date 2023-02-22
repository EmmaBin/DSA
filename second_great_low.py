#Have the function SecondGreatLow(arr) take the array of numbers stored in arr and return the second lowest and second greatest numbers, 
# respectively, separated by a space. For example: if arr contains [7, 7, 12, 98, 106] the output should be 12 98. 
# The array will not be empty and will contain at least 2 numbers. It can get tricky if there's just two numbers!


def SecondGreatLow(arr):
  if len(arr) ==2:
    maxi = max(arr)
    mini = min(arr)
    return str(maxi)+' '+str(mini)
  
  max_num = max(arr)
  min_num = min(arr)
  new_arr=[i for i in arr if i !=max_num and i !=min_num]
  return str(min(new_arr))+' '+str(max(new_arr))


# keep this function call here 
print(SecondGreatLow(input()))