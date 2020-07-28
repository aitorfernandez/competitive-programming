package main

import "testing"

var tests = []struct {
	a      []int
	b      []int
	output []int
}{
	{[]int{1, 2, 2, 1}, []int{2, 2}, []int{2, 2}},
	{[]int{4, 9, 5}, []int{9, 4, 9, 8, 4}, []int{9, 4}},
	{[]int{9, 4, 9, 8, 4}, []int{4, 9, 5}, []int{4, 9}},
	{[]int{1, 2, 2, 1}, []int{2}, []int{2}},
	{[]int{1, 2, 2, 1}, []int{1, 2}, []int{1, 2}},
}

func TestIntersect(t *testing.T) {
	for _, test := range tests {
		got := Intersec(test.a, test.b)

		if len(got) != len(test.output) {
			t.Errorf("got %+v want %+v", got, test.output)
		}

		for i, l := 0, len(got); i < l; i++ {
			if got[i] != test.output[i] {
				t.Errorf("got %+v want %+v", got, test.output)
			}
		}
	}
}
