# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def traverse(root, greatest):
            nonlocal count
            if root is None:
                return
            if root.val >= greatest:
                count +=1
            traverse(root.left, max(root.val, greatest))
            traverse(root.right, max(root.val, greatest))

        traverse(root, -200)
        return count