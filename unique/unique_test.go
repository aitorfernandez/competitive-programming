package unique

import "testing"

var testData = []struct {
	str  string
	want bool
}{
	{
		"abcdef",
		true,
	},
	{
		"aaahy",
		false,
	},
	{
		"abcgghjg",
		false,
	},
}

func TestVerify(t *testing.T) {
	for _, test := range testData {
		got := Verify(test.str)
		if got != test.want {
			t.Fatalf("string %v, got %v want %v", test.str, got, test.want)
		}
	}
}
