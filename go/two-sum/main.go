package main

import "fmt"

func main() {
	// Given an array of integers, return indices of the two numbers such that they add up to a specific target.
	fmt.Println("two-sum")
}

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for i, n := range nums {
		diff := target - n
		if _, ok := m[diff]; ok {
			return []int{m[diff], i}
		}
		m[n] = i
	}

	return []int{}
}
