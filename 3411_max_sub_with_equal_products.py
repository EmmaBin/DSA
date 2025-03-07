class Solution:
    def maxLength(self, nums: List[int]) -> int:
        # how to find the common denominator?
        # how to find the least common multiple?
        result = 1

        def find_lcm(a, b):
            return abs(a*b)//math.gcd(a, b)

        for i in range(len(nums)):
            p = nums[i]
            gcd = nums[i]
            lcm = nums[i]
            for j in range(i+1, len(nums)):
                p *= nums[j]
                gcd = math.gcd(gcd, nums[j])
                lcm = find_lcm(lcm, nums[j])
                if p == gcd*lcm:
                    result = max(result, j-i+1)
        return result
