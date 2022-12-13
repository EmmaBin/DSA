#Example 2: Given a sorted array of unique integers and a target integer, 
# return true if there exists a pair of numbers that sum to target, 
# false otherwise. This problem is similar to Two Sum.

#For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] 
# and target = 13, return true because 4 + 9 = 13.


def check_target(lst, num):
 
  for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):
      if lst[i] + lst[j] == num:
        return True
  return False

print(check_target([1, 2, 4, 6, 8, 9, 14, 15], 13))



def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1
    
    return False