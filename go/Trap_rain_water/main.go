package main

import (
	"fmt"
	"math"
)

func trap(height []int) int {
	lmax := make([]int, len(height))
	rmax := make([]int, len(height))
	lmax[0] = height[0]
	rmax[len(height)-1] = height[len(height)-1]
	for i := 1; i < len(height); i++ {
		lmax[i] = int(math.Max(float64(lmax[i-1]), float64(height[i])))
		rmax[len(height)-i-1] = int(math.Max(float64(rmax[len(height)-i]), float64(height[len(height)-1-i])))
	}
	res := 0
	for i := 1; i < len(height)-1; i++ {
		res = res + int(math.Min(float64(lmax[i]), float64(rmax[i]))) - height[i]
	}
	return res
}

func main() {
	result := trap([]int{7, 1, 5, 3, 6, 4})
	fmt.Println(result)
}
