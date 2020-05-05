package permutation

import "testing"

var testData = []struct {
	a    string
	b    string
	want bool
}{
	{
		"tree",
		"",
		false,
	},
	{
		"dog",
		"god",
		true,
	},
}

func TestPermutaion(t *testing.T) {
	for _, test := range testData {
		got := Permutation(test.a, test.b)
		if got != test.want {
			t.Fatalf("permutation error with %v, %v, got %v, want %v", test.a, test.b, got, test.want)
		}
	}
}
