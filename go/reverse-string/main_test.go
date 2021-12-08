package main

import "testing"

var tests = []struct {
	input  []string
	output []string
}{
	{[]string{"h", "e", "l", "l", "o"}, []string{"o", "l", "l", "e", "h"}},
	{[]string{"H", "a", "n", "n", "a", "h"}, []string{"h", "a", "n", "n", "a", "H"}},
}

func TestReverseString(t *testing.T) {
	for _, test := range tests {
		reverseString(test.input)

		for i, s := range test.input {
			if s != test.output[i] {
				t.Errorf("got %v, want %v", test.input, test.output)
			}
		}
	}
}
