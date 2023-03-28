# Write a function, reverse_list, that takes in the head of a linked list as an argument. 
# The function should reverse the order of the nodes in the linked list in-place and 
# return the new head of the reversed linked list.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def reverse_list(head):
  dummy_head= None
  curr= head
  
  while curr is not None:
    #get in touch with curr.next, after reversing the pointer
    #I don't want to lose contact to the next
    next = curr.next
    #reverse the pointer
    curr.next = dummy_head
    #advance dummy and curr
    dummy_head=curr
    curr=next
  #when it's outbound, curr will be null which was next, dummy will be at tail now
  return dummy_head