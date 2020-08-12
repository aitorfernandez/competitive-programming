package isbn

import (
	"strconv"
)

// IsValidISBN checks if is a valid isbn-10.
func IsValidISBN(isbn string) bool {
	nn, err := check(isbn)
	if err != nil || len(nn) != 10 {
		return false
	}

	var sum int
	for i, n := range nn {
		sum += n * (10 - i)
	}

	if sum%11 == 0 {
		return true
	}
	return false
}

func check(str string) ([]int, error) {
	var nn []int

	for i, s := range str {
		n, err := strconv.Atoi(string(s))
		if err != nil {
			if s == '-' {
				continue
			}
			if s == 'X' && i == len(str)-1 {
				nn = append(nn, 10)
				return nn, nil
			}
			return nn, err
		}

		nn = append(nn, n)
	}

	return nn, nil
}
