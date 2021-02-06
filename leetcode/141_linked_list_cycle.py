#definition for singly-linked list.
class NullPointException(Exception):
    pass

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # Easier to ask for forgivenss than permission
    def hasCycle(self, head: ListNode) -> bool:
       low = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
