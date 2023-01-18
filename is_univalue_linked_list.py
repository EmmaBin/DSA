#Write a function, is_univalue_list, 
# that takes in the head of a linked list as an argument. 
# The function should return a boolean indicating whether 
# or not the linked list contains exactly one unique value.

#You may assume that the input list is non-empty.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def is_univalue_list(head):
    sample = head.val
    curr = head
    while curr is not None:
      if curr.val != sample:
        return False
      curr = curr.next
    return True
  #non-empty
  #given a head of linked list, boolean 
  #high level:
  # investigating if each node val is the same
  # traverse the linked list, get the head.val, 
  #detailed logic:
  # initiate a variable sample = head.val
  # curr = head 
  # start traversing the linked list
  #  while curr is not None:
  #     if curr. val != sample:
  #         return false
  #     curr=curr.next

# n = number of nodes
# Time: O(n)
# Space: O(1)