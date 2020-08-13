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
		return 0, fmt.Errorf("sequences not equal %s, %s", a, b)
	}

	var counter int
	for i := range ar {
		if ar[i] != br[i] {
			counter++
		}
	}

	return counter, nil
}
