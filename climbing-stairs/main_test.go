package main

import "testing"

var tests = []struct {
	input  int
	output int
	des    string
}{
	{2, 2, "There are two ways to climb to the top."},
	{3, 3, "There are three ways to climb to the top."},
}

func TestClimbingStairs(t *testing.T) {
	for _, test := range tests {
		got := ClimbStairs(test.input)
		if got != test.output {
			t.Errorf("got %v, want %v. %s", got, test.output, test.des)
		}
	}
}
