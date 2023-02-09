#https://leetcode.com/problems/fizz-buzz/description/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        #为什么space 是o（1）not O(n)
        result = []
        for i in range(1, n+1):
            if i % 15 ==0:
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result

#这个是错的

#["1","2","Fizz","3","4","Buzz"]
#["1","2","Fizz","4","Buzz"]
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        #为什么space 是o（1）not O(n)
        result = []
        for i in range(1, n+1):
            if i % 15 ==0:
                result.append('FizzBuzz')
            if i % 3 == 0:
                result.append('Fizz')
            if i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result