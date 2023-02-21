#Write a function, path_finder, that takes in the root of a binary tree and a target value. 
#The function should return an array representing a path to the target value. 
#If the target value is not found in the tree, then return None.

#You may assume that the tree contains unique values.#


def path_finder(root, target):
  result = _path_finder(root, target)
  if result is None:
    return None
  else:
    return result[::-1]

def _path_finder(root, target):
  if root is None:
    return None
  if root.val == target:
    return [ target ]
  
  left = _path_finder(root.left, target)
  if left is not None:
    left.append(root.val)
    return left
  
  right = _path_finder(root.right, target)
  if right is not None:
    right.append(root.val)
    return right
  return None