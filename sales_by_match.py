#There is a large pile of socks that must be paired by color. 
# Given an array of integers representing the color of each sock, 
# determine how many pairs of socks with matching colors there are.
#Example: n =7 ar=[1, 2, 1, 2, 3, 2] return: 2


def sockMerchant(n, ar):
    result = 0
    dict = {}
    for i in ar:
        dict[i] = dict.get(i,0)+1
    for value in dict.values():
        
        result += value//2
    return result


