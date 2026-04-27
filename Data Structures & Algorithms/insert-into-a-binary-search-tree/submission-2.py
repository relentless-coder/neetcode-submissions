# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val, None, None)
        return self.traverse(root, node)
    

    def traverse(self, root: Optional[TreeNode], node: Optional[TreeNode]):
        if root is None:
            return node
        if node.val < root.val:
            if root.left:
                self.traverse(root.left, node)
            else:
                root.left = node
        elif node.val > root.val:
            if root.right:
                self.traverse(root.right, node)
            else:
                root.right = node
        return root