package main

import "fmt"

func main() {
	// Given a linked list, determine if it has a cycle in it.
	fmt.Println("linked-list-cycle")
}

// ListNode for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	fastPtr := head
	slowPtr := head

	for fastPtr != nil && fastPtr.Next != nil {
		fastPtr = fastPtr.Next.Next
		slowPtr = slowPtr.Next

		if fastPtr == slowPtr {
			return true
		}
	}
	return false
}
