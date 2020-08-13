package main

import "testing"

var tests = []struct {
	input  []int
	output []int
}{
	{[]int{0, 1, 0, 3, 12}, []int{1, 3, 12, 0, 0}},
	{[]int{1}, []int{1}},
}

func TestMoveZeroes(t *testing.T) {
	for _, test := range tests {
		got := moveZeroes(test.input)

		for i := 0; i < len(got); i++ {
			if got[i] != test.output[i] {
				t.Errorf("got %v, want %w", got, test.output)
			}
		}
	}
}
