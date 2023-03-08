#Write a function, tree_value_count, that takes in the root of a binary tree and a target value. 
#The function should return the number of times that the target occurs in the tree.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_value_count(root, target):
  count = 0
  if root is None:
    return 0

  if root.val == target:
    count +=1
  left = tree_value_count(root.left, target)
  right = tree_value_count(root.right, target)
  return count + left + right



DFS
def tree_value_count(root, target):
  if root is None:
    return 0

  count = 0
  stack = [ root ]
  while stack:
    current = stack.pop()
    if current.val == target:
      count += 1

    if current.left is not None:
      stack.append(current.left)
    if current.right is not None:
      stack.append(current.right)

  return count


BFS
from collections import deque

def tree_value_count(root, target):
  if root is None:
    return 0

  count = 0
  queue = deque([ root ])
  while queue:
    current = queue.popleft()
    if current.val == target:
      count += 1

    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)

  return count