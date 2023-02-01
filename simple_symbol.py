
#Simple Symbols
#Have the function SimpleSymbols(str) take the str parameter being passed 
# and determine if it is an acceptable sequence by either returning the string true or false. 
# The str parameter will be composed of + and = symbols with several characters between them (ie. ++d+===+c++==a) and 
# for the string to be true each letter must be surrounded by a + symbol. 
# So the string to the left would be false. The string will not be empty and will have at least one letter.

def SimpleSymbols(str): 
    import re
    x = re.findall('[a-zA-Z]',str)
    y = re.findall('[+][a-zA-Z][+]',str)
    if len(x)==len(y):
        return 'true'
    else:
        return 'false'
# keep this function call here  
print(SimpleSymbols(input()))


def SimpleSymbols(strParam):
  if strParam[0].isalpha():
    return False
  for i in range(len(strParam)):
    if strParam[i].isalpha():
      if strParam[i-1] != "+" or strParam[i+1] !='+':
        return False


  # code goes here
  return True

# keep this function call here 
print(SimpleSymbols(input()))