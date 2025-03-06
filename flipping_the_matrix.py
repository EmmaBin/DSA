Sean invented a game involving a 2nx2n matrix where each cell of the matrix contains an integer. He can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum of the elements in the
submatrix located in the upper-left quadrant of the matrix. Given the initial configurations for matrices, help Sean reverse the rows and columns of each matrix in the best possible way so that the sum of the elements in the matrix’s upper-left quadrant is maximal.


def flippingMatrix(matrix):
    # Write your code here

    n = len(matrix) // 2
    total = 0

    for i in range(n):
        for j in range(n):
            # Find the maximum value among the four symmetric cells
            max_val = max(
                matrix[i][j],
                matrix[i][2 * n - 1 - j],
                matrix[2 * n - 1 - i][j],
                matrix[2 * n - 1 - i][2 * n - 1 - j]
            )
            total += max_val
    return total
