#Given an integer array nums sorted in non-decreasing order, 
#return an array of the squares of each number sorted in non-decreasing order.
#challenge:  find an O(n) solution 

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

def sortedSquares(self, nums: List[int]) -> List[int]:
    left=0
    right=len(nums)-1
    result=[0]* len(nums)
    for i in range(len(nums)-1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            to_square_num = nums[left]
            left+=1
            
        else:
            to_square_num=nums[right]
            right-=1
        result[i] = to_square_num*to_square_num
    return result
                