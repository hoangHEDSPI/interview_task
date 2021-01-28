import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        priorityQueue = []
        def treeTraversal(self, root: TreeNode):
            if root:
                treeTraversal(root.left)
                heapq.heappush(priorityQueue, root.val)
                treeTraversal(root.right)
        treeTraversal(root)
        return priorityQueue[k-1]


class IterativeSolution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right