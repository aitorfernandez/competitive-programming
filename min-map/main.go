package main

import (
	"fmt"
)

type row map[string]int

func main() {
	fmt.Println("vim-go")
}

func minByColumn(table []row, column string) row {
	out := row{}

	for _, r := range table {
		for k, v := range r {
			if column == k {
				if _, ok := out[k]; ok {
					if out[k] > v {
						out[k] = v
					}
				} else {
					out[k] = v
				}
			} else {
				out[k] = v
			}
		}
	}

	return out
}
