class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        # O(n)
        l = len(nums)
        result = float('inf')
        pre = [float('inf')]*l
        suff = [float('inf')]*l
        for i in range(1, l):
            pre[i] = min(nums[i-1], pre[i-1])
        for j in range(l-2, -1, -1):
            suff[j] = min(nums[j+1], suff[j+1])

        for k in range(1, l-1):
            if nums[k] > pre[k] and nums[k] > suff[k]:
                result = min(result, nums[k]+pre[k]+suff[k])
        if result == float('inf'):
            return -1
        else:
            return result

        # O(n**2)
        result = float('inf')
        for i in range(1, len(nums)-1):
            left = min(nums[:i])
            right = min(nums[i+1:])
            if left < nums[i] and right < nums[i]:
                temp = nums[i]+left+right
                result = min(result, temp)
        if result == float('inf'):
            return -1
        else:
            return result

        # O(n**3)
            # result = float('inf')
        # for i in range(len(nums)-2):
        #     for j in range(i, len(nums)):
        #         if nums[j]>nums[i]:
        #             if j <len(nums)-1:
        #                 for k in range(j, len(nums)):
        #                     if nums[k] < nums[j]:
        #                         temp = nums[i]+nums[j]+nums[k]
        #                         result = min(result,temp)
        # if result == float('inf'):
        #     return -1
        # else:
        #     return result
