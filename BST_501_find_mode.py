# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dict = defaultdict(int)
        def dfs(root, dict):
            if not root:
                return

            dfs(root.left, dict)
            dict[root.val]+=1
            dfs(root.right, dict)
            
        dfs(root, dict)
        result=[]
        count=0
        for key, value in dict.items():
            if value>count:
                count=value
                result=[key]
                #不能写下面这个，因为已经找到更大的了，result就应该只有一个现在找到最大的
                # result.append(key)
            elif count == value:
                result.append(key)
        return result
