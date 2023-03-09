#Write a function, bottom_right_value, that takes in the root of a binary tree. 
#The function should return the right-most value in the bottom-most level of the tree.

#You may assume that the input tree is non-empty.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque
def bottom_right_value(root):
  queue = deque([ root ])
  curr = None
  
  while queue:
    curr = queue.popleft()
    if curr.left:
      queue.append(curr.left)
    if curr.right:
      queue.append(curr.right)
  return curr.val