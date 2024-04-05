# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result =[]

        if root == None:
            return []

        result.extend(self.postorderTraversal(root.left))
        result.extend(self.postorderTraversal(root.right))
        result.append(root.val)
        return result

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)

        return left + right + [root.val]
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        if not root:
            return []
        else:
            stack=[root]
            while stack:
                target = stack.pop()
                if target:
                    result.append(target.val)
                    stack.append(target.left)
                    stack.append(target.right)
                    
                else:
                    continue
        return reversed(result)