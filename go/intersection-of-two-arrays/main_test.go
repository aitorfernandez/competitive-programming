package main

import (
	"reflect"
	"sort"
	"testing"
)

var tests = []struct {
	n1     []int
	n2     []int
	output []int
}{
	{[]int{1, 2, 2, 1}, []int{2, 2}, []int{2, 2}},
	{[]int{4, 9, 5}, []int{9, 4, 9, 8, 4}, []int{4, 9}},
}

func TestIntersect(t *testing.T) {
	for _, test := range tests {
		got := intersect(test.n1, test.n2)

		sort.Ints(got)
		sort.Ints(test.output)
		if !reflect.DeepEqual(got, test.output) {
			t.Errorf("got %v, want %v", got, test.output)
		}
	}
}
