# Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

# Given an integer, find its digit degree.


# For n = 5, the output should be
# solution(n) = 0;
# For n = 100, the output should be
# solution(n) = 1.
# 1 + 0 + 0 = 1.
# For n = 91, the output should be
# solution(n) = 2.
# 9 + 1 = 10 -> 1 + 0 = 1.


def solution(n):
    if len(str(n)) ==1:
        return 0
    result = sum([int(str(i)) for i in str(n)])
    times = 1
    print(result)
    while len(str(result)) >1:
        result = sum([int(str(i)) for i in str(result)])
        times+=1
        print("new", result)
    return times

#第一次没有读懂题，要得到几次