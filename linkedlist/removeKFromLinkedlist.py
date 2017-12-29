class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = none

def removeKFromLinkedlist(l, k):
    fakeHead = ListNode(None)
    fakeHead.next = l
    current = fakeHead
    while current:
        while current.next and current.next.value == k:
            current.next = current.next.next
        current = current.next
    return fakeHead.next



