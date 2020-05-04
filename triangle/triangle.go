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
	isValid := func(v float64) bool {
		if math.IsNaN(v) || math.IsInf(v, 0) || v <= 0 {
			return false
		}
		return true
	}

	ss := []float64{a, b, c}
	for _, s := range ss {
		if !isValid(s) {
			return NaT
		}
	}

	if a+b < c || b+c < a || a+c < b {
		return NaT
	}

	if a == b && b == c {
		return Equ
	}

	if a == b || b == c || c == a {
		return Iso
	}

	return Sca
}
