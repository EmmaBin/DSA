#hourglassSum has the following parameter(s):
#int arr[6][6]: an array of integers
#return: int: the maximum hourglass sum

def hourglassSum(arr):
    #get each hourglass sum, then update max_sum
    #from the requirements, the min number is -9, so -63 is the min
    max_num = -63
    for i in range(len(arr)-2):
        for j in range(len(arr) - 2):
            sum_of_each_hourglass= arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]+arr[i+2][j]+ arr[i+2][j+1] + arr[i+2][j+2]
            if sum_of_each_hourglass > max_num:
                max_num = sum_of_each_hourglass
    return max_num