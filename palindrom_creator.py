#Have the function PalindromeCreator(str) take the str parameter being passed and determine 
#if it is possible to create a palindromic string of minimum length 3 characters by removing 1 or 2 characters. 
#For example: if str is "abjchba" then you can remove the characters jc to produce "abhba" which is a palindrome. 
#For this example your program should return the two characters that were removed with no delimiter and in the order they appear in the string, so jc. 
#If 1 or 2 characters cannot be removed to produce a palindrome, then return the string not possible.

#If the input string is already a palindrome, your program should return the string palindrome. 
#Your program should always remove the characters that appear earlier in the string. 
#In the example above, you can also remove ch to form a palindrome but jc appears first, so the correct answer is jc.

#The input will only contain lowercase alphabetic characters. 
#Your program should always attempt to create the longest palindromic substring by removing 1 or 2 characters (see second sample test case as an example). 
#The 2 characters you remove do not have to be adjacent in the string.

def PalindromeCreator(strParam):


  strCopy = strParam
  TF = True

  if strParam == strParam[::-1]:
    return 'palindrome'
  
  else:
    for i in range(len(strParam)):
      strRemoved = strCopy.replace(strCopy[i],'')
      if strRemoved == strRemoved[::-1] and len(strRemoved) >= 3:
        return strParam[i]
        TF = False
  
    strCopy = strParam
  
    for i in range(len(strParam)):
      strCopy = strParam
      strRemoved1 = strCopy.replace(strCopy[i],'')
      for j in range(len(strRemoved1)):
        strRemoved2 = strRemoved1.replace(strRemoved1[j],'')
        if strRemoved2[::-1] == strRemoved2 and len(strRemoved2) >= 3:
          return strCopy[i] + strRemoved1[j]
          TF = False
  
    if TF:
      return 'not possible'

# keep this function call here 
print(PalindromeCreator(input()))