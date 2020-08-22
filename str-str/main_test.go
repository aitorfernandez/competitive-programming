package main

import "testing"

var tests = []struct {
	haystack string
	needle   string
	output   int
}{
	{"hello", "ll", 2},
	{"aaaaa", "bba", -1},
	{"", "", 0},
	{"mississippi", "pi", 9},
	{"aaaa", "baaa", -1},
}

func TestStrStr(t *testing.T) {
	for _, test := range tests {
		got := strStr(test.haystack, test.needle)
		if got != test.output {
			t.Errorf("got %d, want %d", got, test.output)
		}
	}
}
