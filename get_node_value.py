#Write a function, get_node_value, 
#that takes in the head of a linked list and an index. 
#The function should return the value of the linked list at the specified index.
#If there is no node at the given index, then return None.

def get_node_value(head, index):
  index_count = 0
  current = head
  while current is not None:
    if index_count == index:
      return(current.val)
    else:
      current = current.next
      index_count += 1
      
    
  return None

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def get_node_value(head, index):
  if head is None:
    return None
  if index == 0:
    return head.val
  return get_node_value(head.next, index-1)
#in this recursion way, decreasing the index number, if index is 0, it's the value we are looking for 
