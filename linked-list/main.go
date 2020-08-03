package main

import "fmt"

func main() {
	fmt.Println("linked-list")
}

// Post keeps Post content and pointer to the next Post.
type Post struct {
	Title int
	Next  *Post
}

// Feed struct to manage linked posts.
type Feed struct {
	// Point to the first post.
	Head *Post
	Tail *Post
	Len  int
}

// Append adds a post to Feed.
func (f *Feed) Append(p *Post) {
	// Big-O notation, this algorithm has an O(n) time complexity
	//
	// if f.Len == 0 {
	// 	f.Head = p
	// } else {
	// 	cur := f.Head
	// 	fmt.Println(">>cur.Next", cur.Next)

	// 	// start with the Feed and walk through all the Posts until no Next pointer and attach the new Post.
	// 	for cur.Next != nil {
	// 		cur = cur.Next
	// 	}
	// 	// Attach new Post.
	// 	cur.Next = p
	// }

	// f.Len++

	if f.Len == 0 {
		f.Head = p
		f.Tail = p
	} else {
		// big-O complexity of O(1)
		cur := f.Tail
		cur.Next = p
		f.Tail = p
	}

	f.Len++
}

// Delete deletes a post from the feed.
func (f *Feed) Delete(v int) int {
	if f.Len == 0 {
		return -1
	}

	var prev *Post
	cur := f.Head
	for cur.Title != v {
		if cur.Next == nil {
			return -1
		}

		prev = cur
		cur = cur.Next
	}
	prev.Next = cur.Next

	f.Len--

	return f.Len
}

// Insert inserts a new element by integer title.
func (f *Feed) Insert(p *Post) {
	if f.Len == 0 {
		f.Head = p
		f.Tail = p
	} else {
		var prev *Post
		cur := f.Head

		for cur.Title < p.Title {
			prev = cur
			cur = cur.Next
		}

		prev.Next = p
		p.Next = cur
	}

	f.Len++
}
