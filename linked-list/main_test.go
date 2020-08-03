package main

import "testing"

func TestAppend(t *testing.T) {
	f := &Feed{}
	f.Append(&Post{Title: 1})

	if f.Len != 1 {
		t.Errorf("got %v, want 1", f.Len)
	}

	if f.Head.Title != 1 || f.Tail.Title != 1 {
		t.Errorf("got %v, %v, want 1 for Head and Tail", f.Head.Title, f.Tail.Title)
	}
}

func TestDelete(t *testing.T) {
	f := &Feed{}
	f.Append(&Post{Title: 1})
	f.Append(&Post{Title: 2})

	f.Delete(2)

	if f.Len != 1 {
		t.Errorf("got %v, want 1", f.Len)
	}

	if f.Head.Next != nil {
		t.Errorf("got %+v, want nil", f.Head.Next)
	}
}

func TestInsert(t *testing.T) {
	f := &Feed{}
	f.Append(&Post{Title: 1})
	f.Append(&Post{Title: 5})

	p := &Post{Title: 3}
	f.Insert(p)

	if f.Len != 3 {
		t.Errorf("got %v, want 3", f.Len)
	}

	if f.Head.Next.Title != p.Title {
		t.Errorf("got %v, want %v", f.Head.Next.Title, p.Title)
	}
}
