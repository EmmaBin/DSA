# Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.

# The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.

# Return the blurred image as an integer, with the fractions rounded down.

# For

# image = [[7, 4, 0, 1], 
#          [5, 6, 2, 2], 
#          [6, 10, 7, 8], 
#          [1, 4, 2, 0]]
# the output should be

# solution(image) = [[5, 4], 
#                    [4, 4]]


def solution(image):
    result=[]
    
    for row in range(len(image)-2):
        temp = []
        for col in range(len(image[0])-2):
            total =0
            for inside_row in range(row, row+3):
                for inside_col in range(col, col+3):
                    total += image[inside_row][inside_col]
            total = total // 9
            temp.append(total)
        result.append(temp)
    return result