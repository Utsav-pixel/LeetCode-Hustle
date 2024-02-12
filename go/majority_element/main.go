package main

import (
	"fmt"
)

func majorityElement(nums []int) int {
	counter := make(map[int]int)
	for _, i := range nums {
		if _, ok := counter[i]; ok {
			counter[i]++
			if counter[i] > len(nums)/2 {
				return i
			}

		} else {
			counter[i] = 1
		}

	}
	return nums[0]
}

func main() {
	result := majorityElement([]int{2, 2, 1, 1, 1, 2, 2})
	fmt.Println(result)
}
