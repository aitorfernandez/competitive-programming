package main

import "fmt"

func main() {
	// Given an array, rotate the array to the right by k steps, where k is non-negative.
	fmt.Println("vim-go")
}

func rotate(nums []int, k int) {
	// l := len(nums)
	// k = k % l

	// tmp := nums[l-k:]
	// copy(nums, append(tmp, nums[:l-k]...))

	// Reverse method
	l := len(nums)
	k = k % l

	reverse := func(nums []int, left, right int) {
		for i, j := left, right; i < j; i, j = i+1, j-1 {
			nums[i], nums[j] = nums[j], nums[i]
		}
	}

	reverse(nums, 0, l-1)
	reverse(nums, 0, k-1)
	reverse(nums, k, l-1)
}
