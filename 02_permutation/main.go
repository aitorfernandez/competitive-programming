// Given two strings, write a method to decide if one is a permutation of the other

package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	r := permutation("dog", "god")
	fmt.Println(r)
}

func permutation(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	ss := sortString(s)
	st := sortString(t)

	for i := range ss {
		if ss[i] != st[i] {
			return false
		}
	}

	return true
}

func sortString(s string) []string {
	arr := strings.Split(s, "")
	sort.Strings(arr)

	return arr
}
