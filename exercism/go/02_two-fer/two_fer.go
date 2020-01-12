package twofer

import "fmt"

// ShareWith returns a string with the message One for X, one for me.
func ShareWith(name string) string {
	if name == "" {
		return fmt.Sprint("One for you, one for me.")
	}
	return fmt.Sprintf("One for %v, one for me.", name)
}
