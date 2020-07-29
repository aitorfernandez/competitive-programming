package main

import "testing"

var tests = []struct {
	input  string
	output int
}{
	{"leetcode", 0},
	{"loveleetcode", 2},
}

func TestFirsUniqChar(t *testing.T) {
	for _, test := range tests {
		got := FirstUniqChar(test.input)
		if got != test.output {
			t.Errorf("got %d, want %d", got, test.output)
		}
	}
}
