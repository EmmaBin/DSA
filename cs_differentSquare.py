# Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

# Example

# For

# matrix = [[1, 2, 1],
#           [2, 2, 2],
#           [2, 2, 2],
#           [1, 2, 3],
#           [2, 2, 1]]
# the output should be
# solution(matrix) = 6.

# Here are all 6 different 2 × 2 squares:

# 1 2
# 2 2
# 2 1
# 2 2
# 2 2
# 2 2
# 2 2
# 1 2
# 2 2
# 2 3
# 2 3
# 2 1


def solution(matrix):
    temp=set()
    cols=len(matrix[0])
    rows = len(matrix)
    for i in range(rows-1):
        for j in range(cols-1):
            temp.add((matrix[i][j],matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]))
    return len(temp)