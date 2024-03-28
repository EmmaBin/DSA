


# Given a string, return its encoding defined as follows:

# First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
# for example, "aabbbc" is divided into ["aa", "bbb", "c"]
# Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
# for example, substring "bbb" is replaced by "3b"
# Finally, all the new strings are concatenated together in the same order and a new string is returned.
# Example

# For s = "aabbbc", the output should be
# solution(s) = "2a3bc".



def solution(s):
    sub =s[0]
    result=[]
    n =1
    while n<len(s):
        
        if s[n]==s[n-1]:
            sub += s[n]
        else:
            result.append(sub)
            sub =""
            sub += s[n]
        n+=1
    if len(sub) !=0:
        result.append(sub)
    for i in range(len(result)):
        if len(result[i])>1:
            result[i]= str(len(result[i])) + result[i][0]
        else:
            result[i] = result[i]
    return "".join(result)

            
from itertools import groupby
def solution(s):
    x = ''
    for k,g in groupby(s):
        y = len((list(g)))
        if y==1:
            x += k
        else:
            x += str(y) + k
    return x