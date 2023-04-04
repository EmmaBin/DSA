# Write a function, insert_node, that takes in the head of a linked list, a value, and an index. 
#The function should insert a new node with the value into the list at the specified index. 
#Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

# Do this in-place.

# You may assume that the input list is non-empty and the index is not greater than the length of the input list.


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):
  if index ==0:
    new_head= Node(value)
    new_head.next=head
    return new_head
  
  curr_index = 0
  curr= head
  while curr is not None:
    if curr_index == index-1:
      temp = curr.next
      curr.next=Node(value)
      curr.next.next= temp
      
    curr = curr.next
    curr_index +=1
  return head

#要考虑三点：
#1 如果head 是要被更换的
#2 manipulate pointers 时候，first get a hold of temp, and then link to the temp
#3 是需要create a new node with the value from parameter