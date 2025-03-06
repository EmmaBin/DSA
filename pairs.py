# Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.
def pairs(k, arr):
    result = 0
    arr_set = set(arr)  # 将数组转换为集合

    for element in arr:
        if element + k in arr_set:  # 检查 element + k 是否在集合中
            result += 1

    return result


def pairs(k, arr):
    # Write your code here
    # each element can be used more than once
    # 1,2,3,4,5 k=2
    # 1:3
    # 2:4
    # 3:5
    # 4:6
    # 5:7

    result = 0
    values = {}
    arr_set = set(arr)
    for element in arr:
        values[element] = element+k

    for element, s in values.items():
        if s in arr_set:
            result += 1
    return result
