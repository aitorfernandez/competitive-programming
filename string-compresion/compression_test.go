package compression

import "testing"

var testData = []struct {
	str  string
	want string
}{
	{
		"aaacdeeefghh",
		"a3c1d1e3f1g1h2",
	},
	{
		"aabccccaaa",
		"a2b1c4a3",
	},
	{
		"aabccccrRrr",
		"a2b1c4r4",
	},
}

func TestCount(t *testing.T) {
	for _, test := range testData {
		got := Compress(test.str)
		if got != test.want {
			t.Fatalf("%v got %v want %v", test.str, got, test.want)
		}
	}
}

func BenchmarkCount(b *testing.B) {
	for i := 0; i < b.N; i++ {
		for _, test := range testData {
			_ = Compress(test.str)
		}
	}
}
