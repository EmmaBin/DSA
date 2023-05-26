#https://leetcode.com/problems/merge-sorted-array/

#我在5/26的新理解：两个arr的长度是不一样的时候，很可能其中一个先走完，那先考虑的应该是第二个，因为最后return的
#是第一个，所以只要第二个还有的时候，第一个还有的时候，先把第一个有的copy进去，如果第一个用完了，第二个还有的时候，
#把第二个剩下的全copy到第一个
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #clarify, if any of m or n is 0, return the other
        i = m-1
        j = n-1
        k = m+n-1
        while j>=0:
            if i>=0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k-=1
                i-=1

            else:
                nums1[k] = nums2[j]
                k-=1
                j-=1
        #TC O(m+n)

#这个办法更容易理解，当 m n 都不是零
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    #当m 是0， n 不是0， 那么全都被替代
    nums1[:n] = nums2[:n]  # copying the remaining element at the begining of nums1'


#tail1 reach out to 0 sooner than tail2 , therefore, tail2 must > 0, and we can simply execute the last line code
#tail2 reach out to 0 sonner than tail1, which means at that point, nums1[tail1] < nums2[0] ,
#  and the every element before tail1 of the nums1 is sorted due to the description, 
# That's why we don't need to do anything about the rest tail1.

#hackerrank 上的练习题，不用modify in place
def merge(nums1, nums2):
   
    i=j=k=0
    result = [0]*(len(nums1)+len(nums2))
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            result[k] = nums1[i]
            k+=1
            i+=1
        else:
            result[k]=nums2[j]
            k+=1
            j+=1
    while i<len(nums1):
        result[k] = nums1[i]
        k+=1
        i+=1
    while j<len(nums2):
        result[k] = nums2[j]
        k+=1
        j+=1
    
 
    
    return result