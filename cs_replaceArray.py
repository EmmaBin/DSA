# Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.



# Example

# For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
# solution(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].

#用index去update， 不能for ele in array: if ele ==, ele =. 这样并没有真的改变原有的array，
#ele只是一个copy不是真正的原有在array里的元素
def solution(inputArray, elemToReplace, substitutionElem):
    for i in range(len(inputArray)):
        if inputArray[i] == elemToReplace:
            inputArray[i]= substitutionElem
    return inputArray