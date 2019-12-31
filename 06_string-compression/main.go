// Implement a method to perform basic strings compression using the counts of repeated characters. For example, the string aabccccaaa would become a2b1c4a3

package main

import (
	"fmt"
	"strings"
)

func main() {
	r := compression("aabccccrRrr")
	fmt.Println(r)
}

func compression(str string) string {
	str = strings.ToLower(str)
	count := 0
	output := ""

	for i, s := range str {
		if i+1 == len(str) {
			return format(string(s), output, count+1)
		}

		if string(s) == string(str[i+1]) {
			count++
		} else {
			output = format(string(s), output, count+1)
			count = 0
		}
	}

	return output
}

func format(s, output string, count int) string {
	return fmt.Sprintf("%v%v%v", output, s, count)
}
