#https://leetcode.com/problems/find-k-closest-elements/description/

#always return K length of subarray, k consecutive sublist, 
#so using sliding window would be perfect
#the window left and right slides based on a condition
# this condition is determined by binary search

#The sliding window technique offers a performance advantage over the two-pointer solution, 
#as it doesn't require additional sorting and the time complexity is O(log(n)) 
#due to the binary search approach for sliding the window.

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            # This is a common strategy in binary search to pick the middle element in a range.
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
