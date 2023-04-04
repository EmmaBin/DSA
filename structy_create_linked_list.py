# Write a function, create_linked_list, that takes in a list of values as an argument.
# The function should create a linked list containing each item of the list as the values of the nodes. 
# The function should return the head of the linked list.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
  dummy_node = Node(None)
  curr = dummy_node
  for value in values:
    curr.next = Node(value)
    curr=curr.next
  return dummy_node.next

      
#一边traverse 一边create new linked list