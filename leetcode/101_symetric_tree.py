from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = deque([root])
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val if node is not None else None)
                if node is not None:
                    for child in (node.left, node.right):
                        queue.append(child)
            if level != level[::-1]:
                return False
        return True
