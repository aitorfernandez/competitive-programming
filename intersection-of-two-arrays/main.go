package main

import "fmt"

func main() {
	// Given two arrays, write a function to compute their intersection.
	fmt.Println("intersection-of-two-arrays")
}

func intersect(n1, n2 []int) []int {
	m := make(map[int]int)
	for _, n := range n1 {
		m[n]++
	}

	var res []int
	for _, n := range n2 {
		// don't need check for ok, because the default value if doesn't exists is 0.
		if m[n] > 0 {
			res = append(res, n)
			m[n]--
		}
	}

	return res
}
