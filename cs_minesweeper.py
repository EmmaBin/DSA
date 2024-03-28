# In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

# Example

# For

# matrix = [[true, false, false],
#           [false, true, false],
#           [false, false, false]]
# the output should be

# solution(matrix) = [[1, 2, 1],
#                     [2, 1, 1],
#                     [1, 1, 1]]


def solution(matrix):

    r = []
    
    for i in range(len(matrix)):
        r.append([])
        for j in range(len(matrix[0])):
            l = 0
            
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    #这里是不想考虑matrix[i+x][j+y] 变成matrix[i][j]自己
                    #只考虑周边
                    if x == 0 and y == 0:
                        continue
                    elif 0<=i+x<len(matrix) and 0<=j+y<len(matrix[0]):
                        l += matrix[i+x][j+y]
            #同一 row,新的col advance之前存起来
            r[i].append(l)
    return r