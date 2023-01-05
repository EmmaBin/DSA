#https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right= self.maxDepth(root.right)
        return max(left, right)+1

#O(n) O(n)

#method 2, using BFS and queue, first in and first out
from collections import deque
def maxDepth(self, root):
    if not root:
        return 0
    level =0
    q = deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level +=1
    return level

