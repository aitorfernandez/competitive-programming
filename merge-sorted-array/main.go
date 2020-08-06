package main

import "fmt"

func main() {
	// Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
	fmt.Println("merge-sorted-array")
}

/*
  [1, 2, 3, 0, 0, 0]
  [2, 5, 6]

  Starts for the end and update first array, assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
  first              second
  [1, 2, 3, 0, 0, 6] [2, 5, 6]

  for i = m + n - 1; i >= 0; i-- {
	  // ...
  }
*/

func merge(nums1 []int, m int, nums2 []int, n int) {
	f := m - 1
	s := n - 1

	for i := m + n - 1; i >= 0; i-- {
		if (i >= 0 && s >= 0 && nums1[f] > nums2[s]) || (s < 0) {
			nums1[i] = nums1[f]
			f--
		} else {
			nums1[i] = nums2[s]
			s--
		}
	}
}
