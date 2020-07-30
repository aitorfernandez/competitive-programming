package main

import "testing"

var tests = []struct {
	haystack string
	needle   string
	output   int
}{
	{"hello", "ll", 2},
	{"aaaaa", "bba", -1},
}

func TestStrStr(t *testing.T) {
	for _, test := range tests {
		got := StrStr(test.haystack, test.needle)
		if got != test.output {
			t.Errorf("got %d, want %d", got, test.output)
		}
	}
}
