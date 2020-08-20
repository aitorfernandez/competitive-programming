package main

import "fmt"

func main() {
	// Write a function that reverses a string. The input string is given as an array of characters char[].
	fmt.Println("reverse-string")
}

func reverseString(s []string) {
	left := 0
	right := len(s) - 1

	for left < right {
		temp := s[left]
		s[left] = s[right]
		s[right] = temp

		left++
		right--
	}

	// for left, right := 0, len(s)-1; left < right; left, right = left+1, right-1 {
	// 	s[left], s[right] = s[right], s[left]
	// }
}
