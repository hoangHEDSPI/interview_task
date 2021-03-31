from typing import List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def levelOrderTravesal(self, root):
        queue = []
        queue.append(root)
        self.serializedStr += str(root.val) + "|"
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
                self.serializedStr += str(node.left.val) + "|"
            else:
                self.serializedStr += "N" + "|" # N means None
            if node.right is not None:
                queue.append(node.right)
                self.serializedStr += str(node.right.val) + "|"
            else:
                self.serializedStr += "N" + "|" # N means None
        
    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'N'
        return ','.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])
    
    @staticmethod
    def insertLevelOrder(arr: List[int], root: TreeNode, i, n):
        if i < n:
            temp = TreeNode(arr[i])
            root = temp
            root.left = Codec.insertLevelOrder(arr, root.left, 2*i+1, n)
            root.right = Codec.insertLevelOrder(arr, root.right, 2*i+2, n)
        return root

    def deserialize(self, data) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data is None or len(data) == 0:
            return None
        # assign node values in data to an array
        i = 0
        node_values = []
        while i < len(data):
            j = i
            while j < len(data) and data[j] != '|':
                j += 1
            if data[i:j] != 'N':
                node_values.append(int(data[i:j]))
            else:
                node_values.append(None)
            i = j+1
        root = None
        root = Codec.insertLevelOrder(node_values, root, 0, len(node_values))
        return
        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))