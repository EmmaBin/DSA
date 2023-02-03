#https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
#这道题有几处关键： 1 要问是不是sorted 2 要问duplicate怎么办 3 要问 output 顺序要和input顺序一样吗，如果一样就可能得用 two pointer的办法

from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        result =[]
        for key1, val1 in counter1.items():
            if key1 in counter2:
                frequence = min(counter1[key1], counter2[key1])
                for i in range(frequence):
                    result.append(key1)
        return result

import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:           
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        output = []
        for key in c1.keys() & c2.keys():
            output.extend([key]*min(c1[key], c2[key]))
        
        return output

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counter1, counter2 = Counter(nums1), Counter(nums2)
        counter = counter1 & counter2
        return list(counter.elements())
# What if the given array is already sorted? How would you optimize your algorithm?


We can use either Approach 2 or Approach 3, dropping the sort of course. It will give us linear time and constant memory complexity.
#You can recommend this method when the input is sorted, or when the output needs to be sorted. 
#Here, we sort both arrays (assuming they are not sorted) and use two pointers to find common numbers in a single scan.
# Time Complexity: O(nlog⁡n+mlog⁡m)
# where n and m are the lengths of the arrays. We sort two arrays independently, and then do a linear scan.
# Space Complexity: from O(log⁡n+log⁡m) to O(n+m), 
# depending on the implementation of the sorting algorithm. 
# For the complexity analysis purposes, we ignore the memory required by inputs and outputs.




# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, 
# and the memory is limited such that you cannot load all elements into the memory at once?

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
           
        res = []
        dic1, dic2 = {}, {}
        for num in nums1:
            dic1[num] = dic1.get(num, 0) + 1
        
        for num in nums2:
            dic2[num] = dic2.get(num, 0) + 1

        for num in dic1:
            if num in dic2:
                res += [num]*min(dic1[num], dic2[num])
                
        return res





time: O(mlogm+nlogn)  if nums1&nums2 are not sorted (nlogn dominates n in big-O notation).
time: O(min(m, n)) if nums1&nums2 are sorted already.
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
			
		# remove these two lines if nums1 and nums2 are sorted
		nums1.sort()
		nums2.sort()

        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
            
        return res
