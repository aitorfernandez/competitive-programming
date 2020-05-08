package main

import (
	"fmt"
)

func main() {
	// Given an array, rotate the array to the right by k steps, where k is non-negative.
	fmt.Println("rotate-array")
}

func rotate(nums []int, k int) {
	l := len(nums)
	k %= l

	arr := append(nums[l-k:], nums[:l-k]...)
	copy(nums, arr)

	// var arr []int
	// for i := k; i > 0; i-- {
	// 	arr = append(arr, nums[len(nums)-i])
	// }
	// // nums = nums[:len(nums)-k]
	// copy(nums, append(arr, nums[:len(nums)-k]...))

	// pop
	// x, nums := nums[len(nums)-i], nums[:len(nums)-i]
}
