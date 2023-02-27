#Have the function ExOh(str) take the str parameter being passed and return the string true 
#if there is an equal number of x's and o's, otherwise return the string false. 
#Only these two letters will be entered in the string, no punctuation or numbers. 
#For example: if str is "xooxxxxooxo" then the output should return false 
#because there are 6 x's and 5 o's.

import re
def ExOh(strParam):
  x= len(re.findall('x',strParam))
  o= len(re.findall('o',strParam))


  # code goes here
  return x==o

# keep this function call here 
print(ExOh(input()))


import re
words="xoxo"
print(re.findall('xo',words)) ===>['xo','xo']
#findall return a list