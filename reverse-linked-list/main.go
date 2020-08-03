package main

import "fmt"

func main() {
	fmt.Println("reverse-linked-list")
}

// ListNode definition for likend list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// ReverseList reverse a singly linked list.
func ReverseList(head *ListNode) *ListNode {
	var l *ListNode
	for head != nil {
		l, head, head.Next = head, head.Next, l
	}
	return l
}
