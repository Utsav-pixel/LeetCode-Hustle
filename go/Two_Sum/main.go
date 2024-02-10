package main

import "fmt"

func twoSum(nums []int, target int) []int {
	godict := make(map[int]int)
	for i, num := range nums {
		remaining := target - num
		if idx, ok := godict[remaining]; ok {
			return []int{idx, i}
		}
		godict[num] = i
	}
	return []int{}
}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9
	result := twoSum(nums, target)
	fmt.Println(result)
}
