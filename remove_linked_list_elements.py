#https://leetcode.com/problems/remove-linked-list-elements/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        #head is not val
        dummy=ListNode(None)
        dummy.next = head
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr=curr.next
        return dummy.next



#这道题的重点是一直向前看，check 下一个是不是要找的val
#dummy.next考虑的事，第一个node就是要找的val的话，dummy.next就可以指向新的符合条件的node了