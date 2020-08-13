package main

import "testing"

var tests = []struct {
	input  []int
	output []int
}{
	{[]int{1, 2, 3}, []int{1, 2, 4}},
	{[]int{4, 3, 2, 2}, []int{4, 3, 2, 3}},
	{[]int{9, 9, 9}, []int{1, 0, 0, 0}},
}

func TestPlusOne(t *testing.T) {
	for _, test := range tests {
		got := plusOne(test.input)

		for i := 0; i < len(got); i++ {
			if got[i] != test.output[i] {
				t.Errorf("got %v, want %w", got, test.output)
			}
		}
	}
}
