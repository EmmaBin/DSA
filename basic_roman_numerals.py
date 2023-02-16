#Have the function BasicRomanNumerals(str) read str which will be a string of Roman numerals. 
# The numerals being used are: I for 1, V for 5, X for 10, L for 50, C for 100, D for 500 and M for 1000. 
# In Roman numerals, to create a number like 11 you simply add a 1 after the 10, so you get XI. But to create a number like 19, 
# you use the subtraction notation which is to add an I before an X or V (or add an X before an L or C). So 19 in Roman numerals is XIX.

#The goal of your program is to return the decimal equivalent of the Roman numeral given. 
# For example: if str is "XXIV" your program should return 24


def BasicRomanNumerals(strParam):
  look_up={'I': 1, 'V': 5, 'X':10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}
  numbers = []
  total = 0
  for i in strParam:
    numbers.append(look_up[i])
  for i in range(len(numbers)):
    if i< len(numbers)-1 and numbers[i] < numbers[i+1]:
      numbers[i] = -numbers[i]
    total += numbers[i]
  return total 

  #这道题的关键就是在index 不出界的情况下，如果后面比前面的数字大，前面的数字变负数，然后加起来
  #也要考虑，顺顺利利的时候，就是一个一个加起来