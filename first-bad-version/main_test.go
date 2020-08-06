package main

import "testing"

var tests = []struct {
	vv     []bool
	output int
}{
	{[]bool{false, false, false, false, true, true, true}, 4},
	{[]bool{false, false, true, true}, 2},
}

func TestFirsBadVersion(t *testing.T) {
	for _, test := range tests {
		got := FirstBadVersion(test.vv)
		if got != test.output {
			t.Errorf("got %v, want %v", got, test.output)
		}
	}
}
