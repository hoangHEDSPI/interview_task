# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # iterative version
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            if root.val >= upper or root.val <= lower:
                return False
            stack.append((root.left, lower, root.val))
            stack.append((root.right, root.val, upper))
        return True
