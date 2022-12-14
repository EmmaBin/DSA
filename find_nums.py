#Given an integer array nums,
#find all the numbers x that satisfy the following: x + 1 is not in nums,
#and x - 1 is not in nums


def find_numbers(nums):
    ans = []
    nums = set(nums)

    for num in nums:
        if (num + 1 not in nums) and (num - 1 not in nums):
            ans.append(num)
    
    return ans