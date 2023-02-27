#Have the function ThirdGreatest(strArr) take the array of strings stored in strArr and return the third largest word within it. 
# So for example: if strArr is ["hello", "world", "before", "all"] your output should be world because "before" is 6 letters long, 
# and "hello" and "world" are both 5, but the output should be world because it appeared as the last 5 letter word in the array. 
# If strArr was ["hello", "world", "after", "all"] the output should be after because the first three words are all 5 letters long, 
#so return the last one. 
# The array will have at least three strings and each string will only contain letters.

def ThirdGreatest(arr):
  look_up={}
  for ele in arr:
    if ele not in look_up:
      look_up[ele] = len(ele)
    else:
      continue
  new_look =sorted(look_up.items(), key= lambda x:x[1], reverse=True)
  return new_look[2][0]

# keep this function call here 
print(ThirdGreatest(input()))

#上面这个做法不能pass所有的test case, 比如["hello","world","world"]这里面， world出现两次，第二个就没有办法被记下来

def ThirdGreatest(arr):
   new_arr=sorted(arr, key=lambda x:len(x), reverse=True)
   return new_arr[2]


# keep this function call here 
print(ThirdGreatest(input()))
