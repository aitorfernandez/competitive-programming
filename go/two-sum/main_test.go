package main

import (
	"reflect"
	"testing"
)

var tests = []struct {
	input  []int
	target int
	output []int
}{
	{[]int{2, 7, 11, 15}, 9, []int{0, 1}},
}

func TestTwoSums(t *testing.T) {
	for _, test := range tests {
		got := twoSum(test.input, test.target)

		if !reflect.DeepEqual(got, test.output) {
			t.Errorf("got %v, want %v", got, test.output)
		}
	}
}
