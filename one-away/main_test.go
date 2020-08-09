package main

import "testing"

func TestInvlude(t *testing.T) {
	t.Run("true", func(t *testing.T) {
		got := include("foo", "o")

		if got != true {
			t.Errorf("got %v want true", got)
		}
	})

	t.Run("false", func(t *testing.T) {
		got := include("foo", "b")

		if got != false {
			t.Errorf("got %v want false", got)
		}
	})
}
