# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        totalTilt = 0
        def subTilt(node):
            nonlocal totalTilt
            if not node:
                return 0
            leftSum = subTilt(node.left)
            rightSum = subTilt(node.right)
            tilt = abs(leftSum-rightSum)
            totalTilt += tilt
            return leftSum + rightSum + node.val
        subTilt(root)
        return totalTilt
      
