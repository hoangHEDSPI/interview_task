from Queue import PriorityQueue
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = point = ListNode(None)
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next

if __name__=="__main__":
    a = [1,2,3,4,5]
    q = l = ListNode(None)
    for i in a:
        l.next = ListNode(val=i)
        l = l.next
    while q.next != None:
        print(q.val)
        q = q.next