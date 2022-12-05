#question:
#https://www.hackerrank.com/challenges/minimum-swaps-2/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def minmum_swaps(arr):

    swaps = 0
    lookup = {}

#create a dictionary, index is the key, value is the dict value
    for i, val in enumerate(arr):
        lookup[val] = i

#think about the original postion, 1 is at index 0, if it's not at its original position, swap is happening
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            #create a temporary variable to store the value which is not at its original position
            t = arr[i]
            #rerrange the array to make it at it's original position
            arr[i] = i+1
            #using dictionary index to find out the updated value's index, then arr[index] = temporary number
            #one swap finished
            arr[lookup[i+1]] = t
            #update the dictionary accordingly, no need to think about lookup[i+1]'s value inside the dict, it won't be touched
            lookup[t] = lookup[i+1]d

    return swaps