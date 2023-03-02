#Have the function CorrectPath(str) read the str parameter being passed, 
#which will represent the movements made in a 5x5 grid of cells starting from the top left position. 
#The characters in the input string will be entirely composed of: r, l, u, d, ?. 
#Each of the characters stand for the direction to take within the grid, 
#for example: r = right, l = left, u = up, d = down. 
#Your goal is to determine what characters the question marks should be in order for a path to be created 
#to go from the top left of the grid all the way to the bottom right without touching previously travelled on cells in the grid.

#For example: if str is "r?d?drdd" then your program should output the final correct string 
#that will allow a path to be formed from the top left of a 5x5 grid to the bottom right. 
#For this input, your program should therefore return the string rrdrdrdd. 
#There will only ever be one correct path and there will always be at least one question mark within the input string.

def CorrectPath(strParam):

  # code goes here
  return strParam

# keep this function call here 
print(CorrectPath(input()))


import random
def CorrectPath(str):
    ch=['l', 'u', 'r', 'd']
    str1 = str
    while True:
        x = 1
        y = 1
        emp_str = ''
        pos = []
        for i in str1:
            if i == '?':
                i = random.choice(ch)

            if i == 'l':
                x -= 1
            elif i == 'r':
                x += 1
            elif i == 'u':
                y -= 1
            elif i == 'd':
                y += 1
            #不能越界 0，6
            if x is 0 or x is 6 or y is 0 or y is 6:
                break
            #without touching previously travelled on cells in the grid
            if (x,y) in pos:
                break
            else:
                pos.append((x,y))
                emp_str += i
        #go from the top left of the grid all the way to the bottom right 
        #without touching previously travelled on cells in the grid.
        if x is 5 and y is 5:
            return emp_str
    # code goes here

# keep this function call here
print(CorrectPath(input()))