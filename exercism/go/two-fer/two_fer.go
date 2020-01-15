// Package twofer create a sentence of the form "One for X, one for me.".
package twofer

import "fmt"

// ShareWith returns a string with the message One for X, one for me.
func ShareWith(name string) string {
	var res string
	if name == "" {
		res = "you"
	} else {
		res = name
	}
	return fmt.Sprintf("One for %s, one for me.", res)
}
