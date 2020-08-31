package main

import (
	"fmt"
	"math"
)

func main() {
	// If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
	fmt.Println("best-time-to-buy-and-sell")
}

func maxProfit(prices []int) int {
	minPrice := math.MaxInt32
	maxProfit := 0

	for _, p := range prices {
		if p < minPrice {
			minPrice = p
		} else {
			if p-minPrice > maxProfit {
				maxProfit = p - minPrice
			}
		}
	}

	return maxProfit
}
