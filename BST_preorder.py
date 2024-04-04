# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        if not root:
            return 
        print(root.val)
        #我不懂在这里都有print出来当下的val,也被存在result里面，为什么只有1返回了
        #可能不懂的原因还是不理解recursion每一次如何return value的
        #每一次stack call 是什么样的
        result.append(root.val)
        result.extend(self.preorderTraversal(root.left))
        result.extend(self.preorderTraversal(root.right))
        return result
    

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        return  [root.val] + left +  right