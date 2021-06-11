package main

import "fmt"

func min(a int, b int) int {
	if a > b {
		return b
	}
	return a
}

func minCostClimbingStairs(cost []int) int {
	minimumCost := make([]int, len(cost)+1)
	for i := 2; i < len(cost)+1; i++ {
		takeOneStep := minimumCost[i-1] + cost[i-1]
		takeTwoSteps := minimumCost[i-2] + cost[i-2]
		minimumCost[i] = min(takeOneStep, takeTwoSteps)
	}
	return minimumCost[len(minimumCost)-1]
}

func main() {
	nums := []int{10, 15, 20}
	fmt.Println(minCostClimbingStairs(nums))
}
