/*
Package proverb generates the relevant proverb with a list of inputs.
*/
package proverb

import "fmt"

// Proverb will ouput the full proverbial text based on rhyme array.
func Proverb(rhyme []string) []string {
	var output []string

	if len(rhyme) == 0 {
		return output
	}

	for i := 0; i < len(rhyme)-1; i++ {
		output = append(output, line(rhyme[i], rhyme[i+1]))
	}

	output = append(output, lastLine(rhyme[0]))
	return output
}

func line(a, b string) string {
	return fmt.Sprintf("For want of a %s the %s was lost.", a, b)
}

func lastLine(a string) string {
	return fmt.Sprintf("And all for the want of a %s.", a)
}
