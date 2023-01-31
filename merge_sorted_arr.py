#https://leetcode.com/problems/merge-sorted-array/

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
    nums1[:n] = nums2[:n]  # copying the remaining element at the begining of nums1