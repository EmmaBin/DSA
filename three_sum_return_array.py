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


class Solution:
    def threeSum(self, nums):

        #i != j, i != k, and j != k means only distinct numbers are used
        # we will definitely loop over the array to touch each number but once a number has been considered like 1 and another 1, the second 1 won't be considered, since we have take the first 1 taken into consideration, so we can use sorted array to skip over the duplicate numbers
        nums.sort()
        #now we can loop over a sorted arr, everytime we start using the first number, and find if the there is a pair of the numbers can be 0-firstnumber, we can use two pointer to move inwards to complete testing on one triplets
        #[-4, 0, -1, -1, 1, 2]
        result = []
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                #当index 往前走到这个数字的时候，如果跟上一个数字一样的话，上一个数字已经work完了，
                #就不用再看当下的数字了，所以 continue 到新的下一个数字， i== i-1 是因为上一个已经测完
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s > 0:
                    right -=1
                elif s< 0:
                    left +=1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    #这时候，其他两个数字可能还有组合可以组成符合条件的所以 left 和 right指针还是要走
                    #这个时候还要check要符合条件，并且有相同的数字可以跳过
                    while left <right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    left+=1
                    right -=1

        return result