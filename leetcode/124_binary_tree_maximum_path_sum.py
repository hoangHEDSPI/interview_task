from threading import local
from typing import List
import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # This is a wrong solution because I misunderstood the "path"
    def inorderTraversal(self, root: TreeNode, traversalList: List[int]) -> List[int]:
        if root != None:
            self.inorderTraversal(root.left, traversalList)
            traversalList.append(root.val)
            self.inorderTraversal(root.right, traversalList)
    def maxPathSum(self, root: TreeNode) -> int:
        traversalList = []
        self.inorderTraversal(root=root, traversalList=traversalList)
        # find maximum subarray by Kadane's algorithm
        n = len(traversalList)
        if n == 0:
            return None
        local_max = 0
        global_max = -sys.maxsize - 1
        for i in range(n):
            local_max = max(traversalList[i], traversalList[i] + local_max)
            if local_max > global_max:
                global_max = local_max
        return global_max

class TrueSolution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Placeholder to be updated
        max_path = float('-inf') 

        # get_max_gain of each node
        def get_max_gain(node):
            # Tell to interpereter that max_path is a local variable
            nonlocal max_path
            if node is None:
                return 0
            gain_of_left = max(get_max_gain(node.left), 0)
            gain_on_right = max(get_max_gain(node.right), 0)

            current_max_path = node.val + gain_of_left + gain_on_right
            max_path = max(max_path, current_max_path)
            return node.val + max(gain_of_left, gain_on_right)

        get_max_gain(root)
        return max_path

