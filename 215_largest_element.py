import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        max_l = heapq.nlargest(k, nums)
        return max_l[-1]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_num = min(nums)
        max_num = max(nums)
        counts = [0] * (max_num - min_num + 1)

        # formulate a array counts the frequency of each number
        # this counts array should be sorted from min to max, the value of each position is the frequency
        for number in nums:
            counts[number-min_num] += 1
        # traverse from the biggest number's frequency, k-frequency until k=0

        for i in range(len(counts)-1, -1, -1):
            k = k-counts[i]
            if k <= 0:
                return i+min_num
