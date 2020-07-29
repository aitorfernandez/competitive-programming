package main

import (
	"fmt"
)

func main() {
	// Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
	fmt.Println("first-unique-character")
}

// FirstUniqChar returns the index for the first no-repeating character.
func FirstUniqChar(s string) int {
	// for i := range s {
	// 	// LastIndex from right to left.
	// 	if strings.Index(s, s[i:i+1]) == strings.LastIndex(s, s[i:i+1]) {
	// 		return i
	// 	}
	// }

	m := make(map[rune]int)
	for _, v := range s {
		m[v]++
	}

	for i, v := range s {
		if m[v] == 1 {
			return i
		}
	}

	return -1
}
