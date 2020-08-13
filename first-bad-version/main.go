package main

import "fmt"

func main() {
	// Bynary search
	fmt.Println("first-bad-version")
}

// FirstBadVersion checks which is the last bad version.
func FirstBadVersion(vv []bool) int {
	// left + (right - left ) / 2

	left, right := 1, len(vv)

	for left < right {
		mid := left + (right-left)/2
		// if !isBadVersion(mid, vv) it's more memory expensive
		if vv[mid] {
			right = mid
		} else {
			left = mid + 1
		}
	}

	return left
}
