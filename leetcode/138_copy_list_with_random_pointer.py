from collections import defaultdict
import collections

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # Return a deep copy of the list
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic, prev, node = {}, None, head
        while node:
            if not not in dic:
                dic[node] = Node(node.val, node.next, node.random)
            if prev:
                prev.next = dic[node]
            