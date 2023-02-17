#Have the function StringPeriods(str) take the str parameter being passed and determine if there is some substring K that can be repeated N > 1 times to produce the input string exactly as it appears. 
#Your program should return the longest substring K, and if there is none it should return the string -1.

#For example: if str is "abcababcababcab" then your program should return abcab because that is the longest substring that is repeated 3 times to create the final string. 
#Another example: if str is "abababababab" then your program should return ababab because it is the longest substring. If the input string contains only a single character, 
#your program should return the string -1.

def StringPeriods(strParam):
  if len(strParam) ==1:
    return '-1'
  #can't use set bcz there might be same letters in a substring
  length = len(strParam)
  for factor in range(length // 2, 0, -1):
    if length % factor == 0:
      if strParam[:factor] * (length // factor) == strParam:
        return strParam[:factor]

  return '-1'
  

# keep this function call here 
print(StringPeriods(input()))