# Write a function, zipper_lists, that takes in the head of two linked lists as arguments. 
# The function should zipper the two lists together into single linked list by alternating nodes. 
# If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. 
# The function should return the head of the zippered linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def zipper_lists(head_1, head_2):
  #in the formed new linked list, index at even number are from head_1, odd number are head_2
  #I need two pointers to traverse the two linked list and advance the pointer based on condition
  #need one more pointer to traverse the result linked list(head_1)
  dummy_head= head_1
  counter = 0
  #since modifying in place, head_1 is always gonna be the first 
  curr_1= head_1.next
  curr_2= head_2
  while curr_1 is not None and curr_2 is not None:
    if counter %2==0:
      dummy_head.next = curr_2
      curr_2 = curr_2.next
    else:
      dummy_head.next = curr_1
      curr_1 = curr_1.next
    #while it's still within the bound of two linked lists, after assigning the next
    #node, advance dummy_head pointer, update counter
    counter+=1
    dummy_head = dummy_head.next
  #在做merge two sorted list 时候，如果还是这样写，不用while,就只换了一个，linked list 特点
  #就是pass  进去一个head 就能pass 整条linked list
  if curr_1 is not None:
    dummy_head.next = curr_1
  if curr_2 is not None:
    dummy_head.next = curr_2
  return head_1