package main

import (
	"fmt"
	"sort"
)

const limit int = 3

func main() {
	words := []string{
		"mobile",
		"mouse",
		"moneypot",
		"monitor",
		"mousepad",
	}

	suggestions := keywordSuggestions(words, "mo")
	fmt.Printf("%v", suggestions)
}

func keywordSuggestions(words []string, query string) []string {
	var suggestions []string
	for _, word := range words {
		if query == word[:len(query)] {
			suggestions = append(suggestions, word)
		}
	}

	sort.Sort(sort.StringSlice(suggestions))

	if len(suggestions) < limit {
		return suggestions
	}
	return suggestions[:limit]
}
