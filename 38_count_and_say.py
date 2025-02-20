# iterative

class Solution:
    def countAndSay(self, n: int) -> str:
        def count(str_num):
            result = ""
            i = 0
            while i < len(str_num):
                count = 1
                while i < len(str_num)-1 and str_num[i] == str_num[i+1]:
                    count += 1
                    i += 1

                result += str(count)+str_num[i]
                i += 1
            return result

        prev = "1"
        for i in range(2, n+1):
            prev = count(str(prev))
        return prev
