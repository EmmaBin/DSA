# Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

# Example

# For n = 152, the output should be
# solution(n) = 52;
# For n = 1001, the output should be
# solution(n) = 101.


def solution(n):
    result =[]
    n = str(n)
    for i in range (len(n)):
        temp = int(n[:i]+n[i+1:])
        result.append(temp)
    return max(result)

#不要想的太复杂