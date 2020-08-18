package main

import "testing"

var tests = []struct {
	input  []int
	k      int
	output []int
}{
	{[]int{1, 2, 3, 4, 5, 6, 7}, 3, []int{5, 6, 7, 1, 2, 3, 4}},
	{[]int{-1, -100, 3, 99}, 2, []int{3, 99, -1, -100}},
}

func TestRotate(t *testing.T) {
	for _, test := range tests {
		rotate(test.input, test.k)

		for i, l := 0, len(test.input); i < l; i++ {
			if test.input[i] != test.output[i] {
				t.Errorf("got %v, want %v", test.input, test.output)
			}
		}
	}
}
