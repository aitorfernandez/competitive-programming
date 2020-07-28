/*
Package raindrops convert a number into a string.

The rules of raindrops are that if a given number:

  has 3 as a factor, add 'Pling' to the result.
  has 5 as a factor, add 'Plang' to the result.
  has 7 as a factor, add 'Plong' to the result.
  does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.
*/
package raindrops

import (
	"bytes"
	"strconv"
)

// Convert converts an input number into string.
func Convert(n int) string {
	ff := []struct {
		n   int
		str string
	}{
		{3, "Pling"},
		{5, "Plang"},
		{7, "Plong"},
	}

	var res bytes.Buffer
	for _, f := range ff {
		if n%f.n == 0 {
			res.WriteString(f.str)
		}
	}

	if res.String() == "" {
		return strconv.Itoa(n)
	}

	return res.String()
}
