package main

import (
	"testing"
)

var tests = []struct {
	input  []byte
	output []byte
}{
	{[]byte("hello"), []byte("olleh")},
}

func TestReverseString(t *testing.T) {
	for _, test := range tests {
		ReverseString(test.input)
		for i := 0; i < len(test.input); i++ {
			if test.input[i] != test.output[i] {
				t.Errorf("got %+v, want %+v", test.input, test.output)
			}
		}
	}
}
