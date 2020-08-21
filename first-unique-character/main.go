package main

import "fmt"

func main() {
	// Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
	fmt.Println("first-unique-character")
}

func firstUniqChar(str string) int {
	m := make(map[rune]int)
	for _, s := range str {
		m[s]++
	}

	for i, s := range str {
		if m[s] == 1 {
			return i
		}
	}

	return -1
}
