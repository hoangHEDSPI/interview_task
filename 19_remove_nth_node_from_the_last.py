# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # to perform an one-pass algorithm, instead of using one pointer,
        # we maintain two pointers
        first = second = head
        for _ in range(n):
            first = first.next
        if not first:
            return head.next
        while (first.next != None):
            first = first.next
            second = second.next
        second.next = second.next.next
        return head
