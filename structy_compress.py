#Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'
# You can assume that the input only contains alphabetic characters.

# test_00:
# compress('ccaaatsss') # -> '2c3at3s'

def compress(s):
  s+='!'
  left = right =0
  result =''
  while right <len(s):
    if s[left] == s[right]:
      right+=1

    else:
      counter = right-left
      if counter !=1:
        result+= str(counter)+s[left]
      else:
        result+=s[left]
      left=right
  return result
#我学会的：
#在最开始，我的困难是最后一组一样的字母，在outbound之前，右边指针和左边指针
#永远指的的是一样的，就不会进入到else
#我试过，让右边指针指到最后的时候，在测试几种情况，但太麻烦了，
#最佳办法是人为加东西，加一个不一样的东西，这样就可以正常运作，而不用多家operations,
#很聪明的做法