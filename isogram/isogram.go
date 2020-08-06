/*
Package isogram determines is a word or phrase is an isogram.
*/
package isogram

import "unicode"

// IsIsogram retursn true if the word or phrase is an isogram.
func IsIsogram(str string) bool {
	m := make(map[rune]int)
	for _, s := range str {
		m[unicode.ToLower(s)]++
	}

	for _, s := range str {
		if m[unicode.ToLower(s)] > 1 && !allowCharacter(s) {
			return false
		}
	}

	return true
}

func allowCharacter(r rune) bool {
	if r == '-' || r == ' ' {
		return true
	}
	return false
}
