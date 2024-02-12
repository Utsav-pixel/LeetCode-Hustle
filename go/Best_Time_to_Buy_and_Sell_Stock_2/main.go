package main

import (
	"fmt"
)

func maxProfit(prices []int) int {
	Profit := 0
	for i := 1; i < len(prices); i++ {
		if prices[i] > prices[i-1] {
			Profit = Profit + (prices[i] - prices[i-1])
		}
	}
	return Profit
}

func main() {
	result := maxProfit([]int{7, 1, 5, 3, 6, 4})
	fmt.Println(result)
}
