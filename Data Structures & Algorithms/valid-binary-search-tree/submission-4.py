# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node, mi, ma):
            if node is None:
                return True
            if node.val <= mi or node.val >= ma:
                return False
            return traverse(node.left, mi, node.val) and traverse(node.right, node.val, ma)
        
        return traverse(root, -1000, 1000)