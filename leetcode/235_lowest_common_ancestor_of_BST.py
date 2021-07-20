# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # It's a BST so if p > q then definitely q is on the right branch and vice versa
        if p.val == root.val:
            return p
        if q.val == root.val:
            return q
        
        # Compare p and q with root.val, if p > root.val and q < root.val then return roo.val
        if (p.val > root.val and q.val < root.val) or (p.val < root.val and q.val > root.val):
            return root
        
        # If they are in the same side of root we can call a recursion of lowestCommonAncestor
        if root.left and p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.right and p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
