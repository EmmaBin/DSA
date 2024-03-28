# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.



class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]
        rows = len(image)
        cols = len(image[0])

        def dfs(i, j, grid):
            if i<0 or i>= rows or j<0 or j>= cols:
                return 
            #排除不是同类的 color, 也在排除已经是变成该变的值了
            if starting_color != grid[i][j] or grid[i][j] == color:
                return 
            grid[i][j] = color
            dfs(i+1,j, image)
            dfs(i-1,j, image)
            dfs(i, j+1, image)
            dfs(i,j-1, image)

        dfs(sr, sc, image)
        return image