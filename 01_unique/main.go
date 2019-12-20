// Implement an algorithm to determine if a string has all unique characters

package main

import (
	"fmt"
)

func main() {
	unique := unique("Lorem ipsum dolor")
	fmt.Println(unique)
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

func include(arr []string, s string) bool {
	for _, v := range arr {
		if v == s {
			return true
		}
	}
	return false
}
