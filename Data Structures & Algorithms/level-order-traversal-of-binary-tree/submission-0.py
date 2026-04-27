# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        queue = deque([root])
        level = 0
        while len(queue) > 0:
            tmp = []
            while len(queue) > 0:
                n = queue.popleft()
                if level > (len(res) - 1):
                    res.append([n.val])
                else:
                    res[level].append(n.val)
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            queue = deque(tmp)
            level += 1     
        return res