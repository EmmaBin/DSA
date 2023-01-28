#Have the function EquivalentKeypresses(strArr) 
# read the array of strings stored in strArr which will contain 2 strings representing two comma separated lists of keypresses. 
# Your goal is to return the string true if the keypresses produce the same printable string and the string false if they do not. 
# A keypress can be either a printable character or a backspace represented by -B. 
# You can produce a printable string from such a string of keypresses by having backspaces erase one preceding character.


def EquivalentKeypresses(strArr):
  #two empty strings? -B as in last char inside the str, ignore?
  array1 = strArr[0].split(',')
  array2 = strArr[1].split(',')

  str_1=''
  str_2=''
  for left in array1:
    if left =='-B':
      str_1= str_1[:-1]
    else:
      str_1 += left
    
  for right in array2:
    if right == '-B':
      str_2 = str_1[:-1]
    else:
      str_1 += right
  
  if str_1 == str_2:
    return True
  else:
    return False

#O(n) O(n)
#第一次做的时候，误以为是删去后面的一个，其实是删掉前面的一个，跟正常生活里也是一样的