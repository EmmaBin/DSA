#Given a non-empty binary tree, return the sum of all left leaves.

#这道题注意是所有Leaf left node 
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None
"""
def sum_of_left_leaves(root):
    """
    Write your code here
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    if root.left and not root.left.left and not root.left.right:
        return root.left.val + sum_of_left_leaves(root.right)
    else:
        return sum_of_left_leaves(root.left)+ sum_of_left_leaves(root.right)
root = input_binary_tree()