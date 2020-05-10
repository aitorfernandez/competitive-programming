/*
Package hamming calculate the Hamming Distance between two DNA strands.
*/
package hamming

import "fmt"

// Distance returns the difference between two strands.
func Distance(a, b string) (int, error) {
	// ref: https://blog.golang.org/strings
	ar, br := []rune(a), []rune(b)

	if len(ar) != len(br) {
		return 0, fmt.Errorf("sequences not equal %v, %v", len(a), len(b))
	}

	if a == "" && b == "" {
		return 0, nil
	}

	var counter int
	for i := 0; i < len(ar); i++ {
		if ar[i] != br[i] {
			counter++
		}
	}

	return counter, nil
}
