#https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

def minStartValue(self, nums: List[int]) -> int:
    pre=[nums[0]]
    for i in range (1, len(nums)):
        pre.append(nums[i] + pre[-1])
    min_num= min(pre)
    if min_num > 0:
        return 1
    else:
        return (1-min_num)