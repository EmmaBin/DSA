#https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
   
        #clarification: all lower case, s not empty, k >=1, if k>len(s), return -1
        #return 1 is true, return 0 is false, return any negative number meaningfunction couldn't find the output wanted (indexing).

        #using fixed sized siliding window and prefix method
        #get the first k str to count how many vowels there
        #get hold of the vowels count
        # loop over the rest of the str, 
        # keep adding one element in, delete the first out maintain the size of k
        # while addding and deleting, count the vowels 
        # keep updating the max and return 

        vowels = 'aeiou'
        left = 0
        count=0
        for i in range(0, k):
            if s[i] in vowels:
                count+=1
        #assign to max_count first, later we need to keep track of this max
        max_count = count
        for i in range(k, len(s)):
            if s[i] in vowels:
                count +=1
            if s[left] in vowels:
                count -=1
            left +=1
            max_count = max(count, max_count)
        return max_count


#第二次刷题：
#还有一个情况要考虑，if k>len(s) return -1

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if k>len(s):
            return -1
        count = 0
        vowels='aeiou'
        left=0
        for i in range(0,k):
            if s[i] in vowels:
                count+=1
        result = count 

        for right in range(k, len(s)):
            if s[right] in vowels:
                count+=1
            if s[left] in vowels:
                count-=1
            left+=1

            result = max(count, result)
        return result 
