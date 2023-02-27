#Have the function RectangleArea(strArr) take the array of strings stored in strArr, 
#which will only contain 4 elements and be in the form (x y) where x and y are both integers, 
#and return the area of the rectangle formed by the 4 points on a Cartesian grid. 
#The 4 elements will be in arbitrary order. For example: if strArr is ["(0 0)", "(3 0)", "(0 2)", "(3 2)"] 
#then your program should return 6 because the width of the rectangle is 3 and the height is 2 
#and the area of a rectangle is equal to the width * height.

def RectangleArea(strArr):
  a,b,c,d = strArr
  for i in range(len(a)):
    if a[i] != b[i]:
      width = abs(int(a[i])-int(b[i]))
    if c[i] != d[i]:
      height = abs(int(c[i]) - int(d[i]))
  return width * height

# keep this function call here 
print(RectangleArea(input()))

#以上做法不是全对
#1. For input ["(0 0)", "(3 0)", "(0 2)", "(3 2)"] the output was incorrect. The correct output is 6

#2. For input ["(-1 -1)","(0 0)","(-1 0)","(0 -1)"] the output was incorrect. The correct output is 1

#3. For input ["(-2 -2)","(0 0)","(-2 0)","(0 -2)"] the output was incorrect. The correct output is 4

#4. For input ["(0 0)","(0 0)","(0 0)","(0 0)"] the output was incorrect. The correct output is 0

#5. For input ["(0 0)","(5 0)","(0 3)","(5 3)"] the output was incorrect. The correct output is 15


#第二次 我尝试了新的办法，但是没有想到用index[1]的时候如果有负数就是负数的符号，所以第一步是要把每一个str里的括号处理掉
#变成一个正常格式的list 


def get_coor(s):
  result = s.replace('(','').replace(')','')
  return result.split()
  #get ['0','0']
  
def RectangleArea(strArr):
  x =[]
  y =[]
  for i in range(len(strArr)):
    new_lst = get_coor(strArr[i])

    x.append(int(new_lst[0]))
    y.append(int(new_lst[1]))
  width = max(x) - min(x)
  height = max(y)-min(y)
  return width * height

#用到了helper function, 每一个处理成只有数字的list，把所有x axis放一起，然后y的，就行了。 