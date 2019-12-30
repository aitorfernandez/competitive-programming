// There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two string, write a function to check if they are one edit or zero edits

// pale, ple > true
// pales, pale > true
// pale, bale > true
// pale, bae > false

package main

import "fmt"

func main() {
	result := oneAway("pale", "ple")
	fmt.Printf("pale, ple > %v\n", result)

	result = oneAway("pales", "pale")
	fmt.Printf("pales, pale > %v\n", result)

	result = oneAway("pale", "bale")
	fmt.Printf("pale, bale > %v\n", result)

	result = oneAway("pale", "bae")
	fmt.Printf("pale, bae > %v\n", result)
}

func oneAway(strA, strB string) bool {
	if len(strA) > len(strB) {
		return edit(strA, strB)
	}
	return edit(strB, strA)
}

func edit(strA, strB string) bool {
	counter := 0
	for _, s := range strA {
		if ok := include(strB, string(s)); !ok {
			counter++
		}
	}

	if checkCounter(len(strA)-len(strB), counter) {
		return true
	}
	return false
}

func include(s, x string) bool {
	for _, n := range s {
		if string(n) == x {
			return true
		}
	}
	return false
}

func checkCounter(length, counter int) bool {
	if length == 0 {
		return length+1 == counter
	}
	return length == counter
}
