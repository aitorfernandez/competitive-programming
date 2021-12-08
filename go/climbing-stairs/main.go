package main

import "fmt"

func main() {
	// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
	fmt.Println("climbing-stairs")
}

func climbStairs(n int) int {
	m := make(map[int]int)
	return counting(n, m)
}

func counting(stairs int, m map[int]int) int {
	if stairs < 0 {
		return 0
	}

	if stairs == 0 {
		// sum 1 solution
		return 1
	}

	if m[stairs] != 0 {
		return m[stairs]
	}

	m[stairs] = counting(stairs-1, m) + counting(stairs-2, m)

	return m[stairs]
}
