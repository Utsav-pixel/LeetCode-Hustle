package main

import "fmt"

func twoSum(nums []int, target int) []int {
	goSet := make(map[int]int)
	for i, num := range nums {
		remaining := target - num
		if idx, ok := goSet[remaining]; ok {
			return []int{idx, i}
		}
		goSet[num] = i
	}
	return []int{}
}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9
	result := twoSum(nums, target)
	fmt.Println("Indices of the two numbers:", result) // Output: [0 1]
}
