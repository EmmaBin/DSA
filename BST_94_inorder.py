# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #this method is using recursive way
        result = []
        if root == None:
            return []
        result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))
        return result

#method 2
        result =[]
        def traverse(current_node):
            if not current_node:
                return
            
            traverse(current_node.left)
            result.append(current_node.val)
            
            traverse(current_node.right)
        traverse(root)
        return result
    
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left + [root.val] + right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #stack way
        curr= root
        result =[]
        stack=[]#这里不能提前放root
        if not root:
            return []
        else:
            while stack or curr:
                if curr:
                    stack.append(curr)
                    #一直访问左边点直到尽头
                    curr = curr.left
                else:
                    curr=stack.pop()
                    result.append(curr.val)
                    curr = curr.right
        return result
