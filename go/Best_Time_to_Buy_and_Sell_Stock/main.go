package main

import (
	"fmt"
	"math"
)

func maxProfit(prices []int) int {
	Profit := 0
	BuyAmt := prices[0]
	for i := 1; i < len(prices); i++ {
		if prices[i] < BuyAmt {
			BuyAmt = int(math.Min(float64(prices[i]), float64(BuyAmt)))
		} else {
			Profit = int(math.Max(float64(Profit), float64(prices[i]-BuyAmt)))
		}
	}
	return Profit
}

func main() {
	result := maxProfit([]int{7, 1, 5, 3, 6, 4})
	fmt.Println(result)
}
