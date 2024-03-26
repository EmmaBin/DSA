# Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

# Example

# For inputString = "crazy", the output should be solution(inputString) = "dsbaz".

def solution(inputString):
    result =""
    for s in inputString:
        if s=="z":
            result +="a"
        else:
            
            result+= chr(ord(s)+1)
       
    return result