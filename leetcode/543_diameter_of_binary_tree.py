# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def depth(node: TreeNode) -> int:
            if not node:
                return 0
            l_depth = depth(node.left)
            r_depth = depth(node.right)
            self.ans = max(self.ans, l_depth + r_depth)
            return 1 + max(l_depth, r_depth)
        depth(root)
        return self.ans

class IterativeSolution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_length = 0
        depth = {None: -1}
        stack = [(root, 0)]
        while stack:
            node, visited = stack.pop
            if node is None:
                continue
            if visited == 0:
                stack.extend([(node, 1)], [(node.left, 0)], [(node.right, 0)])
            else:
                left_d = depth[node.left] + 1
                right_d = depth[node.right] + 1
                depth[node] = max(left_d, right_d)
                max_length = max(max_length, depth[node])
        return max_length 