# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            right_side = None
            len_q = len(q)
            for i in range(len_q):
                n = q.popleft()
                if n:
                    right_side = n
                    q.append(n.left)
                    q.append(n.right)
            
            if right_side:
                res.append(right_side.val)
        
        return res
