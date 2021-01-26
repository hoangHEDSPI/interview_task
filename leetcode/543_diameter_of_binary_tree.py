# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def depth(node: TreeNode) -> int:
            if not node:
                return 0
            l_depth = depth(node.left)
            r_depth = depth(node.right)
            self.ans = max(self.ans, l_depth + r_depth)
            return 1 + max(l_depth, r_depth)
        depth(root)
        return self.ans
            
            