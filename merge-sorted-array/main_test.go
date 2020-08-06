package main

import (
	"testing"
)

var tests = []struct {
	nums1  []int
	m      int
	nums2  []int
	n      int
	output []int
}{
	{[]int{1, 2, 3, 0, 0, 0}, 3, []int{2, 5, 6}, 3, []int{1, 2, 2, 3, 5, 6}},
}

func TestMerge(t *testing.T) {
	for _, test := range tests {
		merge(test.nums1, test.m, test.nums2, test.n)

		for i, l := 0, len(test.nums1); i < l; i++ {
			if test.nums1[i] != test.output[i] {
				t.Errorf("got %v, want %v", test.nums1[i], test.output[i])
			}
		}
	}
}
