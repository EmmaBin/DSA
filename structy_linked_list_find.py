#Write a function, linked_list_find, 
#that takes in the head of a linked list and a target value.
#The function should return a boolean indicating whether or not the linked list contains the target.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_find(head, target):
  if head is None:
    return False
  if head.val == target:
    return True

  return linked_list_find(head.next, target)

#head is None condition needs to put first, if head is none, it should be checked first
# return linked_list_find(head.next, target), 有return 这个词

#Space Complexity is O(n), recursion callstack perform takes up O(n)