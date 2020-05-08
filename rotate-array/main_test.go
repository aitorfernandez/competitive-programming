package main

import (
	"testing"
)

var testData = []struct {
	input  []int
	k      int
	output []int
}{
	{
		[]int{1, 2, 3, 4, 5, 6, 7},
		3,
		[]int{5, 6, 7, 1, 2, 3, 4},
	},
	{
		[]int{-1, -100, 3, 99},
		2,
		[]int{3, 99, -1, -100},
	},
	{
		[]int{1, 2},
		3,
		[]int{2, 1},
	},
}

func TestRotate(t *testing.T) {
	for _, test := range testData {
		rotate(test.input, test.k)

		for i := range test.input {
			if test.input[i] != test.output[i] {
				t.Fatalf("invalid output with %v, %v, want %v", test.input, test.k, test.output)
			}
		}
	}
}
