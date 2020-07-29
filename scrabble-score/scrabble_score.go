/*
Package scrabble compute the Scrabble score for a word.

Letter                           Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10

"cabbage" should be scored as worth 14 points:

- 3 points for C
- 1 point for A, twice
- 3 points for B, twice
- 2 points for G
- 1 point for E

And to total:

- `3 + 2*1 + 2*3 + 2 + 1`
- = `3 + 2 + 6 + 3`
- = `5 + 9`
- = 14
*/
package scrabble

import (
	"strings"
)

var letters = map[int][]string{
	1:  []string{"a", "e", "i", "o", "u", "l", "n", "r", "s", "t"},
	2:  []string{"d", "g"},
	3:  []string{"b", "c", "m", "p"},
	4:  []string{"f", "h", "v", "w", "y"},
	5:  []string{"k"},
	8:  []string{"j", "x"},
	10: []string{"q", "z"},
}

// Score returns the Scrabble score.
func Score(str string) int {
	var score int

	if str == "" {
		return score
	}

	str = strings.ToLower(str)

	for _, s := range str {
		for k, v := range letters {
			if in(v, string(s)) {
				score += k
			}
		}
	}

	return score
}

func in(ss []string, v string) bool {
	for _, s := range ss {
		if s == v {
			return true
		}
	}
	return false
}
