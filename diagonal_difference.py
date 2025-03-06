# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9
# The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

# Function description

# Complete the  function in the editor below.

# diagonalDifference takes the following parameter:

# int arr[n][m]: an array of integers
# Return

# int: the absolute diagonal difference
def diagonalDifference(arr):
    n = len(arr)
    total_1 = 0  # 主对角线和
    total_2 = 0  # 副对角线和

    for i in range(n):
        total_1 += arr[i][i]  # 主对角线
        total_2 += arr[i][n - i - 1]  # 副对角线

    return abs(total_1 - total_2)


O(n) and o(1)
