// Implement an algorithm to determine if a string has all unique characters

package main

import (
	"fmt"
)

func main() {
	r := unique("abcde")
	fmt.Println(r)
}

func unique(str string) bool {
	var chars []string
	for _, s := range str {
		if ok := include(chars, string(s)); ok {
			return false
		}
		chars = append(chars, string(s))
	}

	return true
}

func include(a []string, x string) bool {
	for _, n := range a {
		if n == x {
			return true
		}
	}

	return false
}
