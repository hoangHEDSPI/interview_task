# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        
        listValue = []
        while head is not None:
            listValue.append(head.val)
            head = head.next
            
        for i in range(len(listValue)):
            if listValue[i] != listValue[len(listValue)-i-1]:
                return False
        return True