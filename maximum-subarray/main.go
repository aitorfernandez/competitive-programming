package main

import "fmt"

func main() {
	// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
	fmt.Println("maximum-subarray")
}

func maxSubarray(nums []int) int {
	cur, glo := nums[0], nums[0]

	for i, l := 1, len(nums); i < l; i++ {
		cur = max(nums[i], cur+nums[i])
		if cur > glo {
			glo = cur
		}
	}

	return glo
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
