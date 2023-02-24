#Have the function MeanMode(arr) take the array of numbers stored in arr and return 1 if the mode equals the mean, 
# 0 if they don't equal each other (ie. [5, 3, 3, 3, 1] should return 1 because the mode (3) equals the mean (3)). 
# The array will not be empty, will only contain positive integers, and will not contain more than one mode.


from collections import Counter
def MeanMode(arr):
  mean = sum(arr)/len(arr)
  counter = Counter(arr)
  for key, value in counter.items():
    if value == max(counter.values()):
      if key == mean:
        return 1
      else:
        return 0



  # code goes here

# keep this function call here 
print(MeanMode(input()))