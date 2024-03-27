# Given a string, output its longest prefix which contains only digits.

# Example

# For inputString = "123aa1", the output should be
# solution(inputString) = "123".

def solution(inputString):

    
    valid =""
    for s in inputString:
        if s.isdigit():
            valid += s
        else:
            return valid
    return valid

#对什么是prefix的理解，从头开始，一旦不是就不必找了