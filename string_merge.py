#Have the function StringMerge(str) read the str parameter being passed which will contain a large string of alphanumeric characters with a single asterisk character splitting the string evenly into two separate strings. 
# Your goal is to return a new string by pairing up the characters in the corresponding locations in both strings. 
# For example: if str is "abc1*kyoo" then your program should return the string akbyco1o because a pairs with k, b pairs with y, etc. 
# The string will always split evenly with the asterisk in the center.

def StringMerge(strParam):
  #conver to list, *as delimeter
  #loop over the within the range of length since it's the same
  #add it to the result string accordingly
  lst = strParam.split('*')
  lst1=lst[0]
  lst2=lst[1]
  result =''
  for i in range(len(lst1)):
    result +=lst1[i]
    result +=lst2[i]

  # code goes here
  return result

# keep this function call here 
print(StringMerge(input()))