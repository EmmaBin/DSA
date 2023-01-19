#https://leetcode.com/problems/find-the-highest-altitude/description/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #propose prefix_sum technique
        # n>=1
        #return max num of prefix_sum

        # #detailed logic:
        # build a prefix sum list,[0]= 0
        # max(list)
        #O(n) & O(n)
        prefix_sum= [0]

        for i in range(len(gain)):
            prefix_sum.append(gain[i]+prefix_sum[-1])

        return max(prefix_sum)


#method 2: O(n) O(1)

        high_alt = curr_alt = 0
        for alt in gain:
            curr_alt += alt
            if curr_alt > high_alt:
                high_alt = curr_alt
        return high_alt