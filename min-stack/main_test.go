package main

import "testing"

func TestMinStack(t *testing.T) {
	s := New()

	t.Run("Push", func(t *testing.T) {
		v := 1
		s.Push(v)

		if got := s.stack[len(s.stack)-1]; got != v {
			t.Errorf("got %d, want %d", got, v)
		}
	})

	t.Run("Pop", func(t *testing.T) {
		s.Pop()

		if len(s.stack) != 0 {
			t.Errorf("got %d, want 0", len(s.stack))

		}
	})

	t.Run("Top", func(t *testing.T) {
		v := 2
		s.Push(v)

		if got := s.Top(); got != v {
			t.Errorf("got %d, want %d", got, v)
		}
	})

	t.Run("GetMin", func(t *testing.T) {
		min := 2
		s.Push(4)
		s.Push(99)
		s.Push(min)
		s.Push(32)

		if got := s.GetMin(); got != min {
			t.Errorf("got %d, want %d", got, min)
		}
	})
}
