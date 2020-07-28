package main

import "fmt"

func main() {
	fmt.Println("reverse-string")
}

// ReverseString returns a reverse string.
func ReverseString(s []byte) {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
}
