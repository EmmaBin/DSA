
#Letter Capitalize
#Have the function LetterCapitalize(str) take the str parameter being passed 
# and capitalize the first letter of each word. 
# Words will be separated by only one space.#

def LetterCapitalize(strParam):
  param_lst = strParam.split(' ')
  for i in range(len(param_lst)):
    param_lst[i] = param_lst[i][0].upper() + param_lst[i][1:]

  new_str= ' '.join(param_lst)



  # code goes here
  return new_str
  

# keep this function call here 
print(LetterCapitalize(input()))