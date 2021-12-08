package main

import "testing"

var tests = []struct {
	versions []bool
	output   int
}{
	{[]bool{false, false, false, false, true, true}, 4},
	{[]bool{false, true}, 1},
}

func TestFirstBadVersion(t *testing.T) {
	for _, test := range tests {
		got := firstBadVersion(len(test.versions)-1, test.versions)
		if got != test.output {
			t.Errorf("got %d, want %d", got, test.output)
		}
	}
}
