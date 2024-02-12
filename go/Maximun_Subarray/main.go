package main

import (
	"fmt"
	"math"
)

func maxSubArray(nums []int) int {
	MaxSum := nums[0]
	LastSum := nums[0]

	for i := 1; i < len(nums); i++ {
		LastSum = int(math.Max(float64(LastSum+nums[i]), float64(nums[i])))
		MaxSum = int(math.Max(float64(LastSum), float64(MaxSum)))
	}
	return MaxSum
}

func main() {
	result := maxSubArray([]int{7, 1, 5, 3, 6, 4})
	fmt.Println(result)
}
