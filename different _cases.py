
#Have the function DifferentCases(str) take the str parameter being passed and return it in upper camel case format where the first letter of each word is capitalized. 
# The string will only contain letters and some combination of delimiter punctuation characters separating each word.

For example: if str is "Daniel LikeS-coding" then your program should return the string DanielLikesCoding.

def DifferentCases(strParam):
  new_str = strParam.lower()
  new_words =''
  for char in new_str:
    if char.isalpha():
      new_words += char
    else:
      new_words += " "
  new_words = new_words.title()
  return new_words.replace(" ","")


  

# keep this function call here 
print(DifferentCases(input()))