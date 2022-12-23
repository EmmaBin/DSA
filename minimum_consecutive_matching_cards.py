#https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        #find the minimum window to have a matching pair
        # create a hash map{ key is the card[i]: value is the i list}
        # find the value list.length >=2
        # if not existing, return -1, if yes, find the minimum
        groups = defaultdict(list)
        for i in range(len(cards)):
            groups[cards[i]].append(i)
        ans = float("inf")
        for key in groups:

            arr = groups[key]

            #in this for loop, if len(arr) == 1, it will skip this loop,
            #it won't be counted, so it won't to the step of arr[i+1] - arr[i] + 1
            for i in range(len(arr)-1):
                ans = min(ans, arr[i+1]- arr[i] + 1)
        #if ans = 0 
        #find the adjacent difference, length of the a subarray right -left +1

        #if there is ans exist,  小於正無窮
        if ans < float('inf'):
            return ans
        else:
            return -1