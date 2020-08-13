/*
Package permutation decide is one string is permutation of the other.
*/
package permutation

// Permutation check if two strings are permutation.
func Permutation(a, b string) bool {
	if len(a) != len(b) {
		return false
	}

	m := make(map[rune]int)
	for _, r := range a {
		m[r]++
	}

	for _, r := range b {
		if _, ok := m[r]; !ok {
			return false
		}
		m[r]--
		if m[r] < 0 {
			return false
		}
	}

	return true
}

// func Permutation(a, b string) bool {
// 	if len(a) != len(b) {
// 		return false
// 	}

// 	aa := splitAndSort(a)
// 	bb := splitAndSort(b)

// 	for i := range aa {
// 		if aa[i] != bb[i] {
// 			return false
// 		}
// 	}
// 	return true
// }

// func splitAndSort(s string) []string {
// 	arr := strings.Split(s, "")
// 	sort.Strings(arr)

// 	return arr
// }
