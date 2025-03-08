# Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

def gridChallenge(grid):
    # Write your code here
    # rearrage each row
    for i in range(len(grid)):
        l = sorted(list(grid[i]))
        grid[i] = "".join(l)
    # ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy']
    # determine if each col in alpha?
    # (0,0) (1,0)(2,0)(3,0)(4,0)
    # 0,1 1,1 2,1 3,1 4,1
    for col in range(len(grid[0])):
        for row in range(1, len(grid)):
            if grid[row][col] < grid[row-1][col]:
                return "NO"
    return "YES"

# Since we are comparing columns, the outer loop is for the column,
# and the inner loop is for the row. When the column remains fixed,
# we are comparing the rows, with each row being compared to the row above it.
