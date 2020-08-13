/*
Packahe luhn determine is a number is valid per the Luhn formula

Strings of length 1 or less are not valid. Spaces are allowed in the
input, but they should be stripped before checking. All other non-digit
characters are disallowed.

SEE: https://en.wikipedia.org/wiki/Luhn_algorithm
*/

package luhn

import (
	"bytes"
	"strconv"
	"unicode"
)

// Valid valids if input is Luhn formaula.
func Valid(str string) bool {
	str = strip(str)
	if len(str) == 1 || str == "0" {
		return false
	}

	nn, err := atoi(str)
	if err != nil {
		return false
	}

	for i := len(str) - 2; i >= 0; i -= 2 {
		n := nn[i] * 2
		if n > 9 {
			nn[i] = n - 9
		} else {
			nn[i] = n
		}
	}

	return isSumDivisible(nn, 10)
}

func isSumDivisible(nn []int, d int) bool {
	var sum int
	for _, n := range nn {
		sum += n
	}

	if sum%d == 0 {
		return true
	}
	return false
}

func atoi(str string) ([]int, error) {
	var nn []int

	for _, s := range str {
		n, err := strconv.Atoi(string(s))
		if err != nil {
			return nn, err
		}
		nn = append(nn, n)
	}

	return nn, nil
}

func strip(str string) string {
	var buf bytes.Buffer
	for _, s := range str {
		if !unicode.IsSpace(s) {
			buf.WriteRune(s)
		}
	}

	return buf.String()
}
