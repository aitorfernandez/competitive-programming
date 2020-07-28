package main

import "testing"

var tests = []struct {
	nums   []int
	target int
	output []int
}{
	// {[]int{2, 7, 11, 15}, 9, []int{0, 1}},
	{[]int{3, 2, 4}, 6, []int{1, 2}},
}

func TestTwoSum(t *testing.T) {
	for _, test := range tests {
		got := TwoSum(test.nums, test.target)

		if len(got) != len(test.output) {
			t.Errorf("got %+v want %+v", got, test.output)
		}

		for i, l := 0, len(got); i < l; i++ {
			if got[i] != test.output[i] {
				t.Errorf("got %+v want %+v", got, test.output)
			}
		}
	}
}
