#Have the function LetterCountI(str) take the str parameter being passed and return the first word with the greatest number of repeated letters. For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. 
# If there are no words with repeating letters return -1.
#  Words will be separated by spaces.

def LetterCountI(word):
  word_list = word.split(' ')
  max_count = 1
  result = -1
  for word in word_list:
    for letter in word:
      count = word.count(letter)
      if count > max_count:
        max_count = count
        result = word
  return result




# keep this function call here 
print(LetterCountI(input()))