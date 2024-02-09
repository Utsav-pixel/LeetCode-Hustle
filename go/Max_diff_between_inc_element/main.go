package main

import (
	"math"
)

func maximumDifference(nums []int) int {
	i := nums[0]
	max_diff := 0
	for j := 1; j < len(nums); j++ {
		i = int(math.Min(float64(i), float64(nums[j])))
		max_diff = int(math.Max(float64(max_diff), float64(nums[j]-i)))
	}

	if max_diff <= 0 {
		return -1
	}
	return max_diff
}
