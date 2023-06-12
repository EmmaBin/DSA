#Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index.
# Return -1 if the target is not in the array.


# arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
# target = 3
# Output: 1

# Explanation: The first occurrence of 3 is at index 1.

# Input:

# arr = [2, 3, 5, 7, 11, 13, 17, 19]
# target = 6
# Output: -1

def find_first_occurrence(arr: List[int], target: int) -> int:
    l, r = 0, len(arr) - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            ans = mid
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return ans