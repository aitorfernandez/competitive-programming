package main

import "testing"

var tests = []struct {
	input  string
	output int
}{
	{"leetcode", 0},
	{"loveleetcode", 2},
}

func TestFirstUniqChar(t *testing.T) {
	for _, test := range tests {
		got := firstUniqChar(test.input)
		if got != test.output {
			t.Errorf("got %v, want %v", got, test.output)
		}
	}
}
