package main

import "testing"

var tests = []struct {
	input  []int
	output int
}{
	{[]int{2, 2, 1}, 1},
	{[]int{4, 1, 2, 1, 2}, 4},
}

func TestSingleNumber(t *testing.T) {
	for _, test := range tests {
		got := singleNumber(test.input)
		if got != test.output {
			t.Errorf("got %d, want %v", got, test.output)
		}
	}
}
