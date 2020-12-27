# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Handle corner cases
        if head == None or head.next == None:
            return head
        if head.val == head.next.val and head.next.next == None:
            head.next = None
            return head
        
        # In case there are more than two nodes in this given singly-linked list
        cur = head
        while (cur.next != None):
            if cur.val != cur.next.val:
                cur = cur.next
            else:
                cur.next = cur.next.next
        return head