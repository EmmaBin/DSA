# Write a function, remove_node, that takes in the head of a linked list and a target value as arguments.
#The function should delete the node containing the target value from the linked list and return the head of the resulting linked list. 
#If the target appears multiple times in the linked list, only remove the first instance of the target in the list.

# Do this in-place.

# You may assume that the input list is non-empty.

# You may assume that the input list contains the target.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def remove_node(head, target_val):
  #edge cases: 一定会有target _val吗？ 一定会有
  #有多个符合条件怎么办？ 只删掉第一个一样的
  if head.val == target_val:
    return head.next
  curr = head
  prev= None
  
  while curr is not None:
    if curr.val == target_val:
      prev.next = curr.next
      #break 这里很重要，因为根据题的要求，发现到第一个就可以返回了
      break
    prev = curr
    curr = curr.next
  return head