#Have the function ConsonantCount(str) 
# take the str string parameter being passed and return the number of consonants the string contains.


def ConsonantCount(strParam):
  #clarify: empty space uppercase or lowercase, special letter
  not_consonant = 'aeiou'

  count  =0
  for i in strParam.lower():
    if i.isalpha() and i not in not_consonant:
      count +=1


  # code goes here
  return count