#https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b_count = a_count = l_count = o_count = n_count =0
        for letter in text:
            if letter =='b':
                b_count += 1
            if letter =='a':
                a_count +=1
            if letter == 'l':
                l_count += 1
            if letter == 'o':
                o_count +=1
            if letter == 'n':
                n_count += 1
        #注意只要整數， 不然會出現 0.5
        o_count = int(o_count / 2)
        l_count = int(l_count / 2)

        return min(b_count, a_count, l_count, o_count, n_count)