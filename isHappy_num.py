# https://leetcode.com/problems/happy-number/description/

# In this question, there are so many edge cases to be consider
def cal_num(num: int):
	ans = 0
	num = str(num)
	for digit in num:
		ans += int(digit) ** 2
	return ans


class Solution:
	def isHappy(self, n: int) -> bool:
        
		temp = set()

        while n !=1:
            n = cal_num(n)
            if n not in temp:
                temp.add(n)
            else:
                return False
        return True