#Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

# You can assume that the input string is non-empty.

def most_frequent_char(s):
  dict={}
  for letter in s:
    dict[letter]= dict.get(letter,0)+1
  result = None
  for letter in s:
    if result is None or dict[letter] > dict[result]:
      result = letter
  return result

#用最基础的办法得到