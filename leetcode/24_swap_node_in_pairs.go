// Definition for single-linked list
type ListNode struct {
	Val int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode{
	if head == nil || head.Next = nil {
		return head
	}
	result := &ListNode{0, head}
	currentNode := result
	for currentNode.Next != nil && currentNode.Next.Next != nil {
		first := currentNode.Next
		second := first.Next

		temp := second.Next
		second.Next = first
		first.Next = temp
		currentNode.Next = second
		currentNode = currentNode.Next.Next

	}
	return result.Next

}
