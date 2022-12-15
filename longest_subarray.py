#Given an array of positive integers nums and an integer k, 
#find the length of the longest subarray whose sum is less than or equal to k.
#nums = [3, 1, 2, 7, 4, 2, 1, 1, 5] k = 8


#find all the subarrays, use max(0, right-left+1) to return the max length
#(right index - left index + 1) is the length of an array

def longest_subarray(nums, k):
    left=0
    current = 0
    answer =0 

    for right in range(len(nums)):
        current += nums[right]
        while current > k:
            current -= nums[left]
            left+=1
    
        answer = max(0, right-left+1)
    return answer

print(longest_subarray([3, 1, 2, 7, 4, 2, 1, 1, 5],8))
