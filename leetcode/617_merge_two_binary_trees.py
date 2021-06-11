"""
Level Order Traversal of Binary Tree
1. Create an empty queue q
2. temp_node = root 
3. while len(q) > 0:
        print(temp_node.val)
        q.enqueue(temp_node.left)
        q.enqueue(temp_node.right)
        q.dequeue()
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:        
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            ans = TreeNode(root1.val + root2.val)
            ans.left = self.mergeTrees(root1.left,root2.left)
            ans.right = self.mergeTrees(root1.right, root2.right)
            return ans 
        else:
            return root1 or root2

class IterativeSolution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not (root1 or root2):
            return root1 or root2
        root = []
        root.append((root1, root2))
        while root:
            node1, node2 = root.pop()
            if not node2:
                # nothing can be added to node1
                continue
            node1.val += node2.val
            if not node1.left:
                node1.left = node2.left
            else:
                root.append((node1.left, node2.left))
            if not node1.right:
                node1.right = node2.right
            else:
                root.append((node1.right, node2.right))
        return root1