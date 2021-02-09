class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head == None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
    
    def sorted_merge(self, a, b):
        result = None
        if a == None:
            return b
        if b == None:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result
    
    def merge_sort(self, h):
        if h == None or h.next == None:
            return h
        middle = self.get_middle(h)
        next_to_middle = middle.next
        middle.next = None
        left = self.merge_sort(h)
        right = self.merge_sort(next_to_middle)
        sorted_list = self.sorted_merge(left, right)
        return sorted_list
        
    def get_middle(self, head):
        if head == None:
            return head
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow