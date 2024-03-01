#https://leetcode.com/problems/intersection-of-two-linked-lists/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        a_length = get_length(headA)
        b_length = get_length(headB)
        pt1 = headA
        pt2 = headB
        while a_length>b_length:
            pt1=pt1.next
            #这里第一次没有写对，要记得更新长度
            a_length -= 1
        while b_length>a_length:
            pt2=pt2.next
            b_length -= 1
        while pt1 != pt2:
            pt1 = pt1.next
            pt2 = pt2.next
        return pt1



def get_length(head):
    total = 0
    curr = head
    while curr:
        total +=1
        curr = curr.next
    return total





    #这个办法不是特别懂
    #     if not headA or not headB:
    #         return None
        
    #     # 在每个链表的头部初始化两个指针
    #     pointerA = headA
    #     pointerB = headB
        
    #     # 遍历两个链表直到指针相交
    #     while pointerA != pointerB:
    #     # Move pointerA forward by one node
    #         if pointerA is not None:
    #             pointerA = pointerA.next
    #         else:
    #             pointerA = headB

    # # Move pointerB forward by one node
    #         if pointerB is not None:
    #             pointerB = pointerB.next
    #         else:
    #             pointerB = headA
        
    #     # 如果相交，指针将位于交点节点，如果没有交点，值为None
    #     return pointerA