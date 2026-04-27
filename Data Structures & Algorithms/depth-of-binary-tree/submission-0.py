# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def rec(head, curr_depth):
            if head is None:
                return 0
            d = curr_depth
            left_depth = 1 + rec(head.left, d)
            right_depth = 1 + rec(head.right, d)
            return max(left_depth, right_depth)
        return rec(root, depth)
        