package main

func sortArrayByParity(nums []int) []int {
	result := make([]int, len(nums))
	even_index := 0
	odd_index := len(nums) - 1
	for _, v := range nums {
		if v%2 == 0 {
			result[even_index] = v
			even_index += 1
		} else {
			result[odd_index] = v
			odd_index -= 1
		}
	}
	return result
}

func main() {
	nums := []int{3, 2, 1, 4}
	sortArrayByParity(nums)
}
