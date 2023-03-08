#Write a function, five_sort, that takes in a list of numbers as an argument. 
#The function should rearrange elements of the list such that all 5s appear at the end. 
#Your function should perform this operation in-place by mutating the original list. 
#The function should return the list.

#Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the list.


以下不是最优解 但是可行

def five_sort(nums):
  right = len(nums)-1
  left = 0
  while left < right:
    if nums[left] ==5:
      del nums[left]
      nums.append(5)
      right -=1
    else:
      left +=1
  return nums


最优解
def five_sort(nums):
 i = 0
 j = len(nums) - 1
 while i < j:
  if nums[j] == 5:
   j -= 1
  elif nums[i] == 5:
   nums[i], nums[j] = nums[j], nums[i]
   i += 1
  else:
   i += 1
 return nums