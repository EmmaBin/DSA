#Write a function, is_univalue_list, that takes in the head of a linked list as an argument. 
#The function should return a boolean indicating whether or not 
#the linked list contains exactly one unique value.

#You may assume that the input list is non-empty.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def is_univalue_list(head):

  curr = head
  while curr is not None:
    
    if curr.val != head.val:
      return False
    curr = curr.next
  return True


def is_univalue_list(head, prev_val = None):
  #if head is none, meaning it has traversed through the whole linked list, it's at 
  #its tail now, so when tail is None, 就是已经成功全部走完
  if head is None:
    return True
  
  #已经不是第一个node 了， 中间的 
  if prev_val is not None and head.val != prev_val:
    return False
  
  #recursively call itself, 这一次叫head下一个， val 是head自己的val
  return is_univalue_list(head.next, head.val)