#Have the function HammingDistance(strArr) take the array of strings stored in strArr, 
#which will only contain two strings of equal length and return the Hamming distance between them. 
#The Hamming distance is the number of positions where the corresponding characters are different. 
#For example: if strArr is ["coder", "codec"] then your program should return 1. 
#The string will always be of equal length and will only contain lowercase characters from the alphabet and numbers.

def HammingDistance(strArr):
  count = 0
  for i in range(len(strArr[0])):
    if strArr[0][i] != strArr[1][i]:
      count +=1

  # code goes here
  return count

# keep this function call here 
print(HammingDistance(input()))

#这个问题的关键是明白什么是hamming distance, 相同位置不同字母就加一