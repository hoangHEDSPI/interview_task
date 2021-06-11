from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inOrderTraversal(self, root: TreeNode, traversalResult: List[int]):
        if not root:
            return
        self.inOrderTraversal(root.left, traversalResult)
        traversalResult.append(root.val)
        self.inOrderTraversal(root.right, traversalResult)
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        result_1, result_2 = [], []
        self.inOrderTraversal(root1, result_1)
        self.inOrderTraversal(root2, result_2)
        i = j = 0
        while i < len(result_1) and j < len(result_2):
            if result_1[i] <= result_2[j]:
                res += [result_1[i]]
                i += 1
            else:
                res += [result_2[j]]
                j += 1
        
        return res + result_1[i:] + result_2[j:]
        