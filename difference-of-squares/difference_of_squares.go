/*
Package diffsquares find the difference between the square of the sum and the sum of the squares of the first N natural numbers.

The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025.

The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385.

Hence the difference between the square of the sum of the first ten natural numbers and the sum of the squares of the first ten natural numbers is 3025 - 385 = 2640.

https://projecteuler.net/problem=6
*/
package diffsquares

// SquareOfSum returns the square of n numbers.
func SquareOfSum(n int) int {
	var sum int
	for i, l := 1, n+1; i < l; i++ {
		sum += i
	}

	return sum * sum
}

// SumOfSquares returns the squares of n numbers.
func SumOfSquares(n int) int {
	var sum int
	for i, l := 1, n+1; i < l; i++ {
		sum += i * i
	}
	return sum
}

// Difference finds the difference between sqOfSum and sumOfSq.
func Difference(n int) int {
	return SquareOfSum(n) - SumOfSquares(n)
}
