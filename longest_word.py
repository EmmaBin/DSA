#Have the function LongestWord(sen) take the sen parameter being passed and return the longest word 
#in the string. If there are two or more words that are the same length, 
#return the first word from the string with that length. 
#Ignore punctuation and assume sen will not be empty. 
#Words may also contain numbers, for example "Hello world123 567"
def LongestWord(sen):
    nw = ""
    for letter in sen:
      if letter.isalpha() or letter.isnumeric():
        nw += letter
      else :
        nw += " "
    return max(nw.split(),key=len)

#replace special characters with empty space
import re

def LongestWord(sen): 
    sen = re.sub("[^\w\s]", "", sen)
    lst = sen.split()
    max = 0
    max_word = ""
    for i in lst:
      if len(i) > max:
        max = len(i)
        max_word = i
  
    return max_word
    
# keep this function call here  
print(LongestWord(input()))

def LongestWord(sen):
  
  sen_list = sen.split(' ')
  long_word =''
  longest_len = 0
  for word in sen_list:
    cur_word=''
    cur_len=0
    for char in word:
      if char.isalpha() or char.isnumeric():
        cur_word += char
        cur_len+=1
    if cur_len > longest_len:
      longest_len = cur_len
      long_word = cur_word
      
      
    

  return long_word


# keep this function call here 
print(LongestWord(input()))


import re
def LongestWord(sen):
  words=re.split('[^a-z0-9]',sen)
  result = sorted(words, key=lambda x:len(x), reverse=True)



  # code goes here
  return result[0]

# keep this function call here 
print(LongestWord(input()))