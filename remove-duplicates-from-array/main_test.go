package main

import "testing"

var testData = []struct {
	arr    []int
	length int
}{
	{
		[]int{1, 1, 2},
		2,
	},
	{
		[]int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4},
		5,
	},
	{
		[]int{0, 5, 3, 3},
		3,
	},
}

func TestRemoveDuplicates(t *testing.T) {
	for _, test := range testData {
		got := removeDuplicates(test.arr)
		if got != test.length {
			t.Fatalf("got %v, want %v with %v", got, test.length, test.arr)
		}
	}
}
