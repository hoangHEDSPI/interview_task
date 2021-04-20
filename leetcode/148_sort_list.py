# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return
        temp = head
        nodes = []
        while temp:
            nodes.append(temp.val)
            temp = temp.next
        nodes.sort()
        sortedHead = ListNode(nodes[0])
        tempHead = sortedHead
        for i in range(1, len(nodes)):
            tempHead.next = ListNode(nodes[i])
            tempHead = tempHead.next
        return sortedHead