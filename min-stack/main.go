package main

import "fmt"

func main() {
	/*
			Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

		    push(x) -- Push element x onto stack.
		    pop() -- Removes the element on top of the stack.
		    top() -- Get the top element.
		    getMin() -- Retrieve the minimum element in the stack.
	*/

	fmt.Println("min-stack")
}

// MinStack struct.
type MinStack struct {
	stack []int
}

// New returns a new MinStack
func New() *MinStack {
	return &MinStack{}
}

// Push pushs element x onto stack.
func (s *MinStack) Push(x int) {
	s.stack = append(s.stack, x)
}

// Pop removes and returns the elements on top of the stack.
func (s *MinStack) Pop() {
	s.stack = s.stack[:len(s.stack)-1]
}

// Top gets the top element.
func (s *MinStack) Top() int {
	return s.stack[len(s.stack)-1]
}

// GetMin returs the min element in the stack.
func (s *MinStack) GetMin() int {
	min := s.stack[0]
	for _, v := range s.stack {
		if v < min {
			min = v
		}
	}
	return min
}
