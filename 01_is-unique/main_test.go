package main

import "testing"

func TestUnique(t *testing.T) {
	got := unique("abcdef")
	if !got {
		t.Errorf("unique = %v; want true", got)
	}
}

func TestInclude(t *testing.T) {
	a := []string{"t", "e", "s", "t"}
	got := include(a, "t")
	if !got {
		t.Errorf("include = %v; want true", got)
	}
}
