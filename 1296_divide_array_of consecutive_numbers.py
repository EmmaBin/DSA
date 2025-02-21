class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        counter = collections.Counter(nums)
        sorted_keys = sorted(counter.keys())

        for key in sorted_keys:
            while counter[key] > 0:
                for i in range(key, key+k):

                    if counter[i] == 0:
                        return False
                    counter[i] -= 1
        return True
