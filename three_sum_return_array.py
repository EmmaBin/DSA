#https://leetcode.com/problems/3sum/?envType=list&envId=xlem03mm

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1 
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res
    
while j < k and nums[j] == nums[j+1]: j += 1: This line is used to avoid duplicates in the output. Since the array is sorted, any duplicate numbers will be adjacent to each other. If the current number at index j is the same as the next number, j is incremented to skip over all these duplicates. This continues as long as j is less than k (ensuring we don't go out of bounds) and the current number is the same as the next one.

while j < k and nums[k] == nums[k-1]: k -= 1: Similarly, this line skips over duplicates for the k index, moving from right to left. If the current number at index k is the same as the previous number, k is decremented to skip over all these duplicates. This continues as long as k is more than j and the current number is the same as the previous one.

j += 1; k -= 1: After handling duplicates, we need to move the j and k pointers towards each other for the next iteration. We increment j to consider the next element from the left, and decrement k to consider the next element from the right.

These steps ensure that for each i, every pair of j and k is considered exactly once, and duplicates are ignored. This results in the output containing all unique triplets that sum up to zero.