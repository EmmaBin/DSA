#Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:

#<number><char>

#for example, '2c' or '3a'.
#The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.


def uncompress(s):
  #左边指数字，右边指英文字母，这样左右配合才可以
  numbers='0123456789'
  left = right =0
  result =''
  while right <len(s):
    #目标是只要right指的是数字就往前走，当走到字母时候就应该停
    #停到后用slicing 拿到左边指的数字
    if s[right] in numbers:
      right +=1
    else:
      result += int(s[left:right])*s[right]
      right +=1
      left=right
  return result