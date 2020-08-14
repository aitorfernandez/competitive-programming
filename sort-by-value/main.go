package main

import (
	"fmt"
	"sort"
)

func main() {
	colors := map[string]int{
		"red":    50,
		"yellow": 16,
		"blue":   30,
	}
	fmt.Println(colors)

	// By value
	// swap values
	vals := map[int]string{}
	keys := []int{}

	for k, v := range colors {
		// vals[50] = red
		vals[v] = k
		keys = append(keys, v)
	}
	sort.Ints(keys)

	for _, v := range keys {
		fmt.Println(vals[v], v)
	}

	// By key
	// keys := []string{}
	// for k := range colors {
	// 	keys = append(keys, k)
	// }

	// sort.Strings(keys)

	// for _, k := range keys {
	// 	fmt.Println(k, colors[k])
	// }
}
