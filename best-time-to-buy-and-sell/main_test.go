package main

import "testing"

var testData = []struct {
	input  []int
	output int
}{
	{[]int{7, 1, 5, 3, 6, 4}, 5},
	{[]int{7, 6, 4, 3, 1}, 0},
}

func TestMaxProfict(t *testing.T) {
	for _, test := range testData {
		got := maxProfit(test.input)
		if got != test.output {
			t.Fatalf("got %v, want %v for input %v", got, test.output, test.input)
		}
	}
}
