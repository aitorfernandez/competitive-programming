package main

import "testing"

func TestCompression(t *testing.T) {
	e := "a3f1g5e2"
	got := compression("aaafgggggee")
	if e != got {
		t.Errorf("compresion expected %v; got %v", e, got)
	}
}
