package main

import "fmt"

func main() {
	// Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
	fmt.Println("move-zeroes")
}

func moveZeroes(nums []int) []int {
	anchor := 0
	for i, l := 0, len(nums); i < l; i++ {
		if nums[i] != 0 {
			t := nums[anchor]
			nums[anchor] = nums[i]
			nums[i] = t

			anchor++
		}
	}

	return nums
}
