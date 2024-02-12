package main

import (
	"fmt"
)

func check(nums []int) bool {
	inc := 0
	dre := 0

	for i := 0; i < len(nums)-1; i++ {
		if nums[i] < nums[i+1] {
			inc++
		} else if nums[i] > nums[i+1] {
			dre++
		}
	}
	if dre == 0 {
		return true
	} else if inc-dre == inc-1 {
		if nums[0] > nums[len(nums)-1] {
			inc++
		} else if nums[0] < nums[len(nums)-1] {
			dre++
		}
		if inc-dre == inc-1 {
			return true
		}

	}

	return false
}

func main() {
	result := check([]int{3, 4, 5, 7, 4})
	fmt.Println(result)
}
