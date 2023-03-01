#Have the function NextPalindrome(num) take the num parameter being passed and return the next largest palindromic number. 
#The input can be any positive integer. For example: if num is 24, then your program should return 33 
#because that is the next largest number that is a palindrome.


def NextPalindrome(num):
  num += 1
  x = str(num)
  while x != x[::-1]:
    num += 1
    x = str(num)
  return int(x)

print(NextPalindrome(input()))