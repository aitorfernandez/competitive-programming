package main

import "fmt"

func main() {
	// You are climbing a stair case. It takes n steps to reach to the top.
	// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
	fmt.Println("climbing-stairs")
}

// ClimbStairs returns the ways to climb the stairs.
func ClimbStairs(n int) int {
	m := make(map[int]int)
	return counting(n, m)
}

func counting(stairsRemaining int, m map[int]int) int {
	if stairsRemaining < 0 {
		return 0
	}

	if stairsRemaining == 0 {
		// sum 1 valid path
		return 1
	}

	// Use second return value directly in an if statement.
	// if v, ok := m[stairsRemaining]; ok {
	// 	return v
	// }

	// Check for zero value
	if m[stairsRemaining] != 0 {
		return m[stairsRemaining]
	}

	// left and right in the tree
	m[stairsRemaining] = counting(stairsRemaining-1, m) + counting(stairsRemaining-2, m)

	return m[stairsRemaining]
}
