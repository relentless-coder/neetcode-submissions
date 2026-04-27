# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    smallest = None
    count = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverse(root, k)
        return self.smallest

    def traverse(self, root: Optional[TreeNode], k: int):    
        if root is None:
            return None
        self.traverse(root.left, k)
        if self.count < k:
            self.count += 1
        if self.count == k:
            if not self.smallest or root.val < self.smallest:
                self.smallest = root.val
        self.traverse(root.right, k)
