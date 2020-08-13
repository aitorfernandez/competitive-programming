package main

import "fmt"

func main() {
	// Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
	fmt.Println("plus-one")
}

func plusOne(d []int) []int {
	for i := len(d) - 1; i >= 0; i-- {
		if d[i] != 9 {
			d[i]++
			return d
		}
		d[i] = 0
	}

	d = append([]int{1}, d...)
	return d
}
