/*
Package unique determine if a string has all unique characters.
*/
package unique

// Verify checks if all characters are unique.
func Verify(str string) bool {
	var chars []string
	for _, s := range str {
		if ok := include(chars, string(s)); ok {
			return false
		}
		chars = append(chars, string(s))
	}
	return true
}

func include(ss []string, x string) bool {
	for _, s := range ss {
		if s == x {
			return true
		}
	}
	return false
}
