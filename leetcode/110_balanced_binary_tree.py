# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root: TreeNode) -> int:
        if root is None:
            return 0
        leftHeight = self.helper(root.left)
        rightHeight = self.helper(root.right)
        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root) != -1
