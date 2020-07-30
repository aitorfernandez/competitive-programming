package main

import (
	"fmt"
	"strings"
)

func main() {
	// Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
	fmt.Println("str-str")
}

// StrStr returns the first occurrence of needle.
func StrStr(haystack, needle string) int {
	return strings.Index(haystack, needle)
}
