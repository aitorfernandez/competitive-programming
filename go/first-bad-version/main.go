package main

import "fmt"

func main() {
	// Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
	fmt.Println("first-bad-version")
}

func firstBadVersion(n int, vv []bool) int {
	left := 1
	right := len(vv)

	for left < right {
		mid := left + (right-left)/2
		if !vv[mid] {
			left = mid + 1
		} else {
			right = mid
		}
	}

	return left
}
