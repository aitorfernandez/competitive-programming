/*
Package hamming calculate the Hamming Distance between two DNA strands.
*/
package hamming

import "fmt"

// Distance returns the difference between two strands.
func Distance(a, b string) (int, error) {
	if len(a) != len(b) {
		return 0, fmt.Errorf("sequences not equal %v, %v", len(a), len(b))
	}

	if a == "" && b == "" {
		return 0, nil
	}

	var counter int
	for i := range a {
		if a[i] != b[i] {
			counter++
		}
	}

	return counter, nil
}
