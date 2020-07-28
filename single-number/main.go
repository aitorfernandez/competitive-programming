package main

import "fmt"

func main() {
	// Given a non-empty array of integers, every element appears twice except for one. Find that single one.
	fmt.Println("single-number")
}

// SingleNumber returns the single element in an array.
func SingleNumber(nn []int) int {
	for _, n := range nn {
		if in(nn, n) == 1 {
			return n
		}
	}
	return 0
}

func in(nn []int, v int) int {
	var counter int
	for _, n := range nn {
		if n == v {
			counter++
		}
	}
	return counter
}
