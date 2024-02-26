#Given the head of a singly linked list, reverse the list, and return the reversed list.




#Method 1: two pointer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        pre = None
        curr = head
        while curr:
            aftr  = curr.next
            curr.next = pre
            pre = curr
            curr = aftr
        return pre
    

#Method 2: recursion
#Recursion method is actually directly translated from two pointers method.
#First time call the recursion func is to initiate values
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #when first time call this function, it also initialized with values
        return reverse(head, None)

def reverse(curr, prev):
    #here is the base case, or the last step to stop this recursion
    if curr is None:
        return prev
    #Inside each step, we want to have access to aftr pointer, and reverse the direction
    #when call func itself, we are actually moving forward bt assigning new pointers, which are one step forward then curr pointers

    aftr = curr.next
    curr.next=prev
    return reverse(aftr, curr)
    