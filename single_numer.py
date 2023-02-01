#https://leetcode.com/problems/single-number/description/

def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key

def singleNumber2(self, nums):
    res = 0
    for num in nums:
        res ^= num
    return res
    
#Space complexity : O(n+n)=O(n)
#set needs space for the elements in nums


def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)

    
def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)
    
def singleNumber(self, nums):
    return reduce(operator.xor, nums)
#https://leetcode.com/problems/single-number/solutions/690738/python-o-1-space-simple-solution-with-detailed-explanation/?orderBy=most_votes&languageTags=python

# a^=b is equivalent to: a = a ^ b
# where ^ means XOR

        for i in range(1,len(nums)):
            nums[0] ^= nums[i]
        return nums[0]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ## RC ##
        ## APPROACH : XOR ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##
        
        # If we take XOR of zero and some bit, it will return that bit
        # a XOR 0 = a, a XOR 0=a
        # If we take XOR of two same bits, it will return 0
        # a XOR a = 0 a XOR a=0
        # a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b 
        # a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
        # So we can XOR all bits together to find the unique number.
        
        a = 0
        for i in nums:
            a ^= i
        return a