#https://leetcode.com/problems/maximum-average-subarray-i/description/

def findMaxAverage(self, nums: List[int], k: int) -> float:
    left=curr_total=0
    average=0
    for right in range(k):   
        curr_total+= nums[right]
    average = curr_total/k
    
    for right in range(k, len(nums)):
        curr_total= curr_total + nums[right]-nums[left]
        left+=1
        average = max(average, curr_total/k)
    return average