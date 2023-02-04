#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_prof = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            max_prof = max(max_prof, (price-min_price))
        return max_prof



#some thing new I learned from this question:
#1. float('inf') infinity used to initialize and update to find the minimum number
#2. in this question, loop over the array once, while looping, keep holding of the min
# price, and update the max_profit using max built-in method.


# Two point
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #update left pointer to the newest low 
        #then proceed the right pointer to one direction

        left = 0
        right =1
        max_p = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                right +=1
            else:
                max_p = max(max_p, prices[right]- prices[left])
                right+=1
        return max_p


def findMaxProfit(arr):

  maxProfit = 0
  minPrice = arr[0]

  for i in range(1, len(arr)):
    currProfit = arr[i] - minPrice 
    maxProfit = max(maxProfit, currProfit)
    minPrice = min(minPrice, arr[i])

  return maxProfit