package main

import "fmt"

func main() {
	// Given a linked list, determine if it has a cycle in it.
	fmt.Println("linked-list-circle")
}

// ListNode definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return false
	}

	slow := head
	fast := head.Next

	for slow != nil && fast != nil {
		if slow.Val == fast.Val {
			return true
		}

		if fast.Next == nil {
			return false
		}

		fast = fast.Next.Next
		slow = slow.Next
	}

	return false
}
