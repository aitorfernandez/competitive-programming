package main

import "fmt"

func main() {
	// Given an array of integers, return indices of the two numbers such that they add up to a specific target.
	fmt.Println("two-sum")
}

// TwoSum returs the indices of the sum of two numbers.
func TwoSum(nums []int, target int) []int {
	m := make(map[int]int, len(nums))
	for i, n := range nums {
		if j, ok := m[target-n]; ok {
			return []int{j, i}
		}

		m[n] = i
	}

	return []int{}

	// l := len(nums)
	// for i := 0; i < l; i++ {
	// 	for j := 0; j < l; j++ {
	// 		if j == i {
	// 			continue
	// 		}
	// 		if nums[i]+nums[j] == target {
	// 			return []int{i, j}
	// 		}
	// 	}
	// }

	// return []int{}
}
