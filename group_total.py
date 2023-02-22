#Have the function GroupTotals(strArr) read in the strArr parameter containing key:value pairs where the key is a string and the value is an integer. 
# Your program should return a string with new key:value pairs separated by a comma such that each key appears only once with the total values summed up.

#For example: if strArr is ["B:-1", "A:1", "B:3", "A:5"] then your program should return the string A:6,B:2.

#Your final output string should return the keys in alphabetical order. Exclude keys that have a value of 0 after being summed up.

#每一个list里的element还是要用 ‘：’来分一下，变成list,因为不确定字母有多长
#还要注意，把dictionary里面的keys 存放在已经sorted的list里面，作为reference,这样loop over and retrive the value from dictionary
#to build a new result list and join them together
def GroupTotals(strArr):
  look_up={}
  result =[]
  for ele in strArr:
    new_ele= ele.split(':')
    if new_ele[0] not in look_up:
      look_up[new_ele[0]] = int(new_ele[1])
    else:
      look_up[new_ele[0]] += int(new_ele[1])

  new_list = sorted(list(look_up.keys()))
  for key in new_list:

    if look_up[key]!=0:
      result.append(f'{key}:{look_up[key]}')

    
  


  return ','.join(result)




  # code goes here
  # return strArr

# keep this function call here 
print(GroupTotals(input()))