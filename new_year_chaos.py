# One person can bribe at most two others.
#Determine the minimum number of bribes that took place to get to a given queue order. 
# Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

#solution1 missed some corner case, such as [1 2 5 3 7 8 6 4], '4' is not taken into account
def minimumBribes(q):
    
    bribe = 0
    jump = 0 
    for i in range(len(q)):
        if q[i] > i:
            if q[i]-1-i >2:
                print('Too chaotic')
                return
            else:
                jump = q[i]-1 -i
                bribe+= jump
    print(bribe)
    return

#solution 2 
def minimumBribes(q):
    
    bribes = 0
    last_item = len(q)
    while len(q)!=0:
        count = 0
        for i in range(len(q)-1, len(q)-4, -1):
            if q[i] == last_item:
                bribes+= count
                q.pop(i)
                break
            elif count ==2:
                print('Too chaotic') 
                return
            else:
                count +=1
        last_item = len(q)
        
    print (bribes)