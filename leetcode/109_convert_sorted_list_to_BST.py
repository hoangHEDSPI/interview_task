# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def constructBSTFromList(list_node: List[int]):
            if not list_node:
                return None
            mid = len(list_node) // 2
            root = ListNode(list_node[mid])
            root.left = constructBSTFromList(list_node[:mid])
            root.right = constructBSTFromList(list_node[mid+1:])
            return root
        
        if not head:
            return None
        list_node = []
        temp_head = head
        while temp_head != None:
            list_node.append(temp_head.val)
            temp_head = temp_head.next
        return constructBSTFromList(list_node)
  
