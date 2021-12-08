package main

import "fmt"

func main() {
	// Given a non-empty array of integers, every element appears twice except for one. Find that single one.
	fmt.Println("single-number")
}

func singleNumber(nums []int) int {
	// Bit manipulation
	v := 0
	for _, n := range nums {
		// a XOR 0 = a
		// a XOR a = 0
		// a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b
		v = v ^ n
	}

	return v

	// m := make(map[int]bool)

	// for _, n := range nums {
	// 	m[n] = !m[n]
	// }

	// for k, v := range m {
	// 	if v {
	// 		return k
	// 	}
	// }

	// return 0
}
