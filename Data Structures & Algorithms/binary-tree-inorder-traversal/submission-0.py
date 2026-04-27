# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = [];
        self.traverse(root, l)
        return l

    def traverse(self, root: Optional[TreeNode], l: List[int]):
        if root is None:
            return None
        
        self.traverse(root.left, l)
        l.append(root.val)
        self.traverse(root.right, l)