package main

import "fmt"

func main() {
	// Merge two sorted linked lists and return it as a new sorted list.
	fmt.Println("merge-two-lists")
}

// ListNode for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// MergeTwoLists returns a new ListNode.
func MergeTwoLists(a, b *ListNode) *ListNode {
	l := &ListNode{}
	head := l

	for a != nil || b != nil {
		if a == nil {
			head.Next = b
			break
		}

		if b == nil {
			head.Next = a
			break
		}

		if a.Val <= b.Val {
			head.Next = a
			a, head = a.Next, head.Next
		} else {
			head.Next = b
			b, head = b.Next, head.Next
		}
	}

	return l.Next
}
