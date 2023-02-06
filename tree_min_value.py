#Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. 
#The function should return the minimum value within the tree.

#You may assume that the input tree is non-empty.

from collections import deque
def tree_min_value(root):
  queue = deque([root])
  result = float('inf')
  while queue:
    curr = queue.popleft()
    result = min(result, curr.val)
    if curr.left:
      queue.append(curr.left)
    if curr.right:
      queue.append(curr.right)
  return result

def tree_min_value(root):
    if root is None:
        return float('inf')
    curr = root.val
    result = float('inf')
    result = min(result, curr)
    return min(root.val, tree_min_value(root.left), tree_min_value(root.right))