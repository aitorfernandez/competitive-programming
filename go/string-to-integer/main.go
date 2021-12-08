package main

import (
	"fmt"
	"math"
	"strconv"
	"unicode"
)

func main() {
	fmt.Println("string-to-integer")
}

func myAtoi(str string) int {
	n := ""
Loop:
	for _, s := range str {
		switch {
		case
			unicode.IsNumber(s),
			(s == '+' || s == '-') && len(n) == 0:
			n += string(s)
		case unicode.IsSpace(s) && len(n) > 0:
			break Loop
		case unicode.IsSpace(s):
			break
		default:
			break Loop
		}
	}

	i, _ := strconv.Atoi(n)
	switch {
	case i < math.MinInt32:
		return math.MinInt32
	case i > math.MaxInt32:
		return math.MaxInt32
	}

	return i
}
