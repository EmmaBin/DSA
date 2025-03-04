class Solution:
    def isUgly(self, n: int) -> bool:

        if n <= 0:
            return False
        primes = [2, 3, 5]
        while n != 1:
            factor = 0
            for num in primes:
                if n % num == 0:
                    n = n/num
                    factor = num
            if factor == 0:
                return False
        return True

# method 2 - recursion

        while n != 1:
            if n % 2 == 0:
                n = n/2
            elif n % 3 == 0:
                n = n/3
            elif n % 5 == 0:
                n = n/5
            else:
                return False
        return True
