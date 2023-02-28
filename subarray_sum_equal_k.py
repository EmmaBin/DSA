#https://leetcode.com/problems/subarray-sum-equals-k/description/

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1
    
        return ans


from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        preSum = 0
        counter = defaultdict(int)

        for num in nums:
            preSum += num
            
            # instead of initiate counter[0] with 1
            if preSum == k:
                res += 1

            if preSum - k in counter:
	            res += counter[preSum - k]

            counter[preSum] += 1

        return res