
#https://leetcode.com/problems/number-of-good-pairs/description/
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = {}
        res = 0
        for number in nums:            
            if number in hashMap:
                res += hashMap[number]
                hashMap[number] += 1
            else:
                hashMap[number] = 1
        return res


#If the value already exists in the hashMap that means 
# the number of new pairs is equal to the frequency since the current value 
# can be paired with each prior occurrence .

    def numIdenticalPairs(self, nums: List[int]) -> int:
        hmap,count = {},0
        for i,num in enumerate(nums):
            if num in hmap:
                count += len(hmap[num])
                hmap[num].append(i)
            else:
                hmap[num] = [i]
        return count

        from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        countDict = defaultdict(int)
        total = 0
        for num in nums: 
            total += countDict[num]
            countDict[num] += 1
        return total