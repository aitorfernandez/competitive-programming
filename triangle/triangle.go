/*
Package triangle determine if a triangle is equilateral, isosceles, or scalene.
*/
package triangle

import (
	"math"
)

// Kind is int type.
type Kind int

const (
	// NaT for Not a Triangle.
	NaT = iota
	// Equ for Equilateral.
	Equ
	// Iso for Isosceles.
	Iso
	// Sca for Scalene.
	Sca
)

// KindFromSides determine type of triangle.
func KindFromSides(a, b, c float64) Kind {
	// isValid check for a shape to be a triangle.
	// isValid := func(v float64) bool {
	// 	if math.IsNaN(v) || math.IsInf(v, 0) || v <= 0 {
	// 		return false
	// 	}
	// 	return true
	// }

	// ss := []float64{a, b, c}
	// for _, s := range ss {
	// 	if !isValid(s) {
	// 		return NaT
	// 	}
	// }

	switch {
	case a*b*c <= 0, a+b < c, b+c < a, a+c < b, math.IsInf(a+b+c, 1), math.IsNaN(a + b + c):
		return NaT
	case a == b && b == c:
		return Equ
	case a == b, b == c, c == a:
		return Iso
	default:
		return Sca
	}
}
