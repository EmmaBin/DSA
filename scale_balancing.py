#Have the function ScaleBalancing(strArr) read strArr which will contain two elements, 
#the first being the two positive integer weights on a balance scale (left and right sides) 
#and the second element being a list of available weights as positive integers. 
#Your goal is to determine if you can balance the scale by using the least amount of weights from the list, 
#but using at most only 2 weights. For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"] 
#then this means there is a balance scale with a weight of 5 on the left side and 9 on the right side. 
#It is in fact possible to balance this scale by adding a 6 to the left side from the list of weights and adding a 2 to the right side. 
#Both scales will now equal 11 and they are perfectly balanced. Your program should 
#return a comma separated string of the weights that were used from the list in ascending order, 
#so for this example your program should return the string 2,6

#There will only ever be one unique solution and the list of available weights will not be empty. 
#It is also possible to add two weights to only one side of the scale to balance it. 
#If it is not possible to balance the scale then your program should return the string not possible.



import itertools
def ScaleBalancing(a):
    x = eval(a[0])
    y = eval(a[1])
    for a in y: 
        #Test if one weight can balance the scale
        if x[0] + a == x[1] or x[1] + a == x[0]:
            return str(a)
        #Test if two weights can balance the scale
    for pair in list(itertools.combinations(y, 2)):
        if pair[0] + x[0] == x[1] + pair[1] or pair[0] + x[1] == pair[1] + x[0] or pair[0] + pair[1] + x[0] == x[1] or pair[0] + pair[1] + x[1] == x[0]:
            l, i = min(pair), max(pair)
            return ','.join([str(l), str(i)])
    return 'not possible'
print(ScaleBalancing(input()))