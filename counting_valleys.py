#A mountain is a sequence of consecutive steps above sea level,
# starting with a step up from sea level and ending with a step down to sea level.
#A valley is a sequence of consecutive steps below sea level, 
# starting with a step down from sea level and ending with a step up to sea level.
#Given the sequence of up and down steps during a hike, 
# find and print the number of valleys walked through.
#Eg, steps = 8 path=[DDUUUUDD] returns: 2 the number of valley treaversed

def countingValleys(steps, path):
    # Write your code here
    count = 0
    result =0
    for word in path:
        if word =="U":
            count +=1
        else: 
            count -=1
        if count == 0 and word == "U":
            result += 1
    return result