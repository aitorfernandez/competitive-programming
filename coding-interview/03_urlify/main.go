// Write a method to replace all spaces in a string with %20

package main

import (
	"fmt"
	"strings"
)

func main() {
	r := urlify("lorem ipsum dolor")
	fmt.Println(r)
}

func urlify(s string) string {
	return strings.Replace(s, " ", "%20", -1)
}
