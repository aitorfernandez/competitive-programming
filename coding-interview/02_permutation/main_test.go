package main

import "testing"

func TestSortString(t *testing.T) {
	e := []string{"e", "s", "t", "t"}
	got := sortString("test")

	for i := range e {
		if e[i] != got[i] {
			t.Errorf("sortString expected %v; got %v", e, got)
		}
	}
}
