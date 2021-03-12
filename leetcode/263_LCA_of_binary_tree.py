from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """Find the LCA of two node p and q in a TreeNode
        Args:
         - root
         - p
         - q
        Return the LCA value
        """
        if root == p or root == q:
            return root
        left = right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both children returned a node, meaning either p or q found on left or right branch
        if left and right:
            return root
        else:
            return left or right