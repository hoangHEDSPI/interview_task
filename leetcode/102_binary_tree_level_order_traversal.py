from typing import List
import queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result, level = [], [root]
        while root and level:
            result.append([node.val for node in level])
            leftRightPair = [(node.left, node.right) for node in level]
            level = [leaf for LR in leftRightPair for leaf in LR if leaf]
        return result

# What if I use a FIFO queue to solve this problem
# And what if I use a deque
class QueueSolution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q, result = queue.Queue(), []
        if root:
            q.put(root)
        while not q.empty:
            level = []
            