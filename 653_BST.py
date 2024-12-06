class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        q = deque([root])
        while q:
            node = q.popleft()
            if k - node.val in seen:
                return True
            
            seen.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False