#Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. 
#Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). 
#Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.


def LetterChanges(strParam):
  letters="abcdefghijklmnopqrstuvwxyza"
  vowels='aeiou'
  result =''
  temp=[]
  for a in strParam:
    if a.isalpha():
      idx = letters.index(a)
      temp.append(letters[idx+1])
    else:
      temp.append(a)
  for char in temp:
    if char in vowels:
      result +=char.upper()
    else:
      result += char
    



  # code goes here
  return result