/*
Package compression perform basic strings compression using the counts of repeated characters.

For example, the string aabccccaaa would become a2b1c4a3.
*/
package compression

import (
	"fmt"
	"strconv"
	"strings"
)

// Compress returns the compression string.
func Compress(str string) string {
	str = strings.ToLower(str)

	var count int
	// var output string
	var output strings.Builder

	for i, s := range str {
		if i+1 == len(str) {
			output.WriteString(string(s))
			output.WriteString(strconv.Itoa(count + 1))
			break

			// return format(output, string(s), count+1)
		}

		// rune vs byte
		if string(s) == string(str[i+1]) {
			count++
		} else {
			output.WriteString(string(s))
			output.WriteString(strconv.Itoa(count + 1))

			// output = format(output, string(s), count+1)
			count = 0
		}
	}
	// return output
	return output.String()
}

func format(o, s string, count int) string {
	return fmt.Sprintf("%v%v%v", o, s, count)
}
