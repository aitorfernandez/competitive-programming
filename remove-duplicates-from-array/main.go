package main

import (
	"sort"
)

func main() {
	// Given an array nums, remove the duplicates in-place such that each element appear only once and return the new length.
}

func removeDuplicates(nums []int) int {
	sort.Ints(nums)

	var counter int

	for i := len(nums) - 1; i > 0; i-- {
		if nums[i] == nums[i-1] {
			counter++
		} else {
			nums = append(nums[:i], nums[i+counter:]...)
			counter = 0
		}
	}

	nums = nums[counter:] // remove first positions.

	return len(nums)

	// Faster version...
	// p1 := 0
	// for p2, l := 1, len(nums); p2 < l; p2++ {
	// 	if nums[p1] != nums[p2] {
	// 		p1++
	// 		nums[p1] = nums[p2]
	// 	}
	// }
	// return p1 + 1
}
