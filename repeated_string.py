#There is a string,s , 
# of lowercase English letters that is repeated infinitely many times. 
# Given an integer, n, 
# find and print the number of letter a's in the first  letters of the infinite string.
#Eg, s='abcac' n=10 return: the frequency of a in the substring

def repeatedString(s, n):
    num_of_s = (n//len(s))
    a_in_s = s.count('a')
    almost_a = num_of_s*a_in_s
    remainder_a= s[:n%(len(s))].count('a')
    return almost_a + remainder_a