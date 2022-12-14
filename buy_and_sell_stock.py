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