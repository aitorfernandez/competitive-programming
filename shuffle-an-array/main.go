package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	// Shuffle a set of numbers without duplicates.
	fmt.Println("shuffle-an-array")

	obj := NewSolution([]int{1, 2, 3})
	fmt.Println(obj.Reset())
	fmt.Println(obj.Shuffle())
}

// Solution struct keeps
type Solution struct {
	nums []int
}

// NewSolution returns a new Solution struct.
func NewSolution(nums []int) *Solution {
	return &Solution{nums}
}

// Reset returs the original nums in Solution.
func (s *Solution) Reset() []int {
	return s.nums
}

// Shuffle the nums Solution.
func (s *Solution) Shuffle() []int {
	nums := make([]int, len(s.nums))
	copy(nums, s.nums)

	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(len(nums), func(i, j int) { nums[i], nums[j] = nums[j], nums[i] })

	// for i := len(s.nums) - 1; i > 0; i-- {
	// 	j := rand.Intn(i + 1)
	// 	s.nums[i], s.nums[j] = s.nums[j], s.nums[i]
	// }

	return nums
}
