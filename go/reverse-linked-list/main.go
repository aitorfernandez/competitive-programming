package main

import "fmt"

func main() {
	// Reverse a singly linked list.
	fmt.Println("reverse-linked-list")
}

// ListNode for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var l *ListNode
	for head != nil {
		l, head, head.Next = head, head.Next, l
	}

	return l
}
