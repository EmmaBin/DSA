#https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
		# swap if str2 longer than str1
        str1, str2 = (str1, str2) if len(str1) >= len(str2) else (str1, str2)
        len_str1 = len(str1)
        len_str2 = len(str2)
		# check if str1 == str2 * k
        if str2 * int(len_str1 / len_str2) == str1:
            return str2
        best = ''
		# prefix couldn't be longer than int(len_str2 / 2), exept it full word, wich we check already
        for i in range(1, int(len_str2 / 2) + 1):
			# check if prefix str2 * k == str2 and  prefix str2 * k == str1 (from shortest to longest) 
            if str2[:i] * int(len_str2 / len(str2[:i])) == str2 and str2[:i] * int(len_str1 / len(str1[:i])) == str1:
                best = str2[:i]
        return best