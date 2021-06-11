# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root.right:
            self.bstToGst(root.right)
        root.val = self.pre = self.pre + root.val
        if root.left:
            self.bstToGst(root.left)
        return root