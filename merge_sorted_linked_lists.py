#https://leetcode.com/problems/merge-two-sorted-lists/

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2):

        
    #create a dummy head node, None as its value
    dummy_head = Node(None)
    #tail also points to dummy_head, it's task is to traverse 
    #the linked list
    tail = dummy_head
    #initiate variables to pointing to two heads
    curr_1= head_1
    curr_2= head_2
    while curr_1 is not None and curr_2 is not None:
        if curr_1.val < curr_2.val:
            tail.next = curr_1
            curr_1 = curr_1.next
        else:
            tail.next = curr_2
            curr_2 = curr_2.next
        tail=tail.next

    if curr_2 is not None:
        tail.next = curr_2
    if curr_1 is not None:
        tail.next = curr_1

    return dummy_head.next

#TC O(min(m,n))只取最短的，因为长的多出来的部分，直接加在后面
#sc： 0（1） 没有用多余的地方，in place