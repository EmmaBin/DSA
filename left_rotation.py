#rotLeft has the following parameter(s):
#int a[n]: the array to rotate
#int d: the number of rotations
#return: int a'[n]: the rotated array
#eg: 5 4
#1 2 3 4 5
#return: 5 1 2 3 4






def rotLeft(a, d):
    # Write your code here
    arr=[]
    arr.extend(a[d:])
    arr.extend(a[:d])
    return arr