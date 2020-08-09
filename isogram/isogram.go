/*
Package isogram determines is a word or phrase is an isogram.
*/
package isogram

import "unicode"

// IsIsogram retursn true if the word or phrase is an isogram.
func IsIsogram(str string) bool {
	repeated := make(map[rune]bool)
	for _, s := range str {
		r := unicode.ToLower(s)

		if r == '-' || r == ' ' {
			continue
		}

		if repeated[r] {
			return false
		}

		repeated[r] = true
	}

	return true
}
