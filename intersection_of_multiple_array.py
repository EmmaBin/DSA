#https://leetcode.com/problems/intersection-of-multiple-arrays/description/


from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res=[]
        #distinct meaning only appears once in each integer array,
        #create a hash map of this nums array, if any number appears
        #the amount of the total integer array, that is the number returned 

        counts = defaultdict(int)
        for i in nums:
            for x in i:
                counts[x] +=1
        
        nums_length= len(nums)
        for key in counts:
            if counts[key] == nums_length:
                res.append(key)

        return sorted(res)



#algorithm has a space complexity of O(n⋅m)