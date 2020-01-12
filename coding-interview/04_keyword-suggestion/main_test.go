package main

import (
	"fmt"
	"testing"
)

func TestKeywordSuggestions(t *testing.T) {
	cities := []string{
		"Edinburgh",
		"Barrie",
		"Ebina",
		"Barshi",
		"Okazaki",
		"Basel",
		"Reno",
	}

	check := func(got, want interface{}) {
		if fmt.Sprintf("%v", got) != fmt.Sprintf("%v", want) {
			t.Errorf("got %v want %v", got, want)
		}
	}

	t.Run("return limit", func(t *testing.T) {
		got := keywordSuggestions(cities, "Ba")
		want := [3]string{
			"Barrie",
			"Barshi",
			"Basel",
		}

		check(got, want)
	})

	t.Run("return less than limit", func(t *testing.T) {
		got := keywordSuggestions(cities, "O")
		want := [1]string{"Okazaki"}

		check(got, want)
	})
}
