package main

import "testing"

var tests = []struct {
	input  []int
	output int
	des    string
}{
	{[]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}, 6, "[4,-1,2,1] has the largest sum = 6."},
}

func TestMaxSubarray(t *testing.T) {
	for _, test := range tests {
		got := maxSubarray(test.input)
		if got != test.output {
			t.Errorf("got %v, want %d %s", got, test.input, test.des)
		}
	}
}
