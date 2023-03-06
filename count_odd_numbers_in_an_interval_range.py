#https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
#这道题第一想法是用 range,然后一个数一个数去算是不是奇数，这样TC就会是0(n)当数字是很大的时候就不行le
#找到的规律就是，其实在两个数字之间 有一半肯定是奇数，然后看首位的两个数字有一个说奇数 我们再加一就行了
#重点是观察规律

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Initialize odd with the number of even numbers between low and high.
        odd = (high - low) // 2
        
        # If either low or high is odd, increment odd by 1.
        if low % 2 == 1 or high % 2 == 1:
            odd += 1
        
        # Return the number of odd numbers between low and high.
        return odd