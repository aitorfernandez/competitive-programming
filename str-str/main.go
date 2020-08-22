package main

import (
	"fmt"
)

func main() {
	// Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
	fmt.Println("str-str")
}

func strStr(haystack, needle string) int {
	// i := strings.Index(haystack, needle)
	if len(needle) == 0 {
		return 0
	}

	for i, j := 0, len(needle); i+len(needle)-1 < len(haystack); i, j = i+1, j+1 {
		if haystack[i:j] == needle {
			return i
		}
	}

	return -1
}
