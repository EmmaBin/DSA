#Given the head of a singly linked list, return true if it is a palindrome
#or false otherwise.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes =[]
        curr= head
        while curr:
            nodes.append(curr.val)
            curr=curr.next
        if nodes == nodes[::-1]:
            return True
        else:
            return False