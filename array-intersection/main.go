package main

import "fmt"

func main() {
	// Given two arrays, write a function to compute their intersection.
	fmt.Println("array-intersection")
}

// Intersec returns the intersection.
func Intersec(numsA, numsB []int) []int {
	m := make(map[int]int)
	for _, n := range numsA {
		// count the number of times appear the number.
		// map[n:1, n+1:1...]
		m[n]++
	}

	var res []int
	for _, n := range numsB {
		if m[n] > 0 {
			res = append(res, n)
			m[n]--
		}
	}

	return res
}
