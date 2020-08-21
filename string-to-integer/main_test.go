package main

import "testing"

var tests = []struct {
	input  string
	output int
}{
	{"42", 42},
	{"   -42", -42},
	{"4193 with words", 4193},
	{"words and 987", 0},
	{"-91283472332", -2147483648},
	{"3.141559", 3},
	{"  -0012a42", -12},
	{"  +0 123", 0},
	{"-5-", -5},
}

func TestMyAtoi(t *testing.T) {
	for _, test := range tests {
		got := myAtoi(test.input)
		if got != test.output {
			t.Errorf("got %v, want %v", got, test.output)
		}
	}
}
