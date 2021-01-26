from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    """
    @param preorder: a list of integers
    @param inorder: a list of integers
    @return: a tree node
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """The idea is to find the root first, and then recursively build 
        each left and right subtree
        """
        if not preorder or not inorder:
            return None
        rootValue = preorder[0]
        root = TreeNode(rootValue)
        inorderIndex = inorder.index(rootValue)
        root.left = self.buildTree(preorder[1:inorderIndex+1], inorder[:inorderIndex])
        root.right = self.buildTree(preorder[inorderIndex+1:], inorder[inorderIndex+1:])
        return root
    
    def optimizedBuildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        rootValue = preorder.pop(0)
        root = TreeNode(rootValue)
        inorderIndex = inorder.index(rootValue)
        root.left = self.optimizedBuildTree(preorder, inorder[:inorderIndex])
        root.right = self.optimizedBuildTree(preorder, inorder[inorderIndex+1:])
        
        return root
    
    
