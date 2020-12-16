// Suppose that we have an array X that equals to [1,2,3,4]
// Seeing this problem from graph perspective, we can re-form this problem to the problem of
// finding all the path from vertex i -> vertex j (i and j two values on array X) through all other vertexes
// For example, if we start from 1 and and end at 4, we have 1->2->3->4 and 1->3->2->4 as two only valid paths
// And we can solve this problem by using DFS

func permute(nums []int) [][]int {
	if len(nums) == 0 {
		return nil
	}

	ans := make([][]int, 0)
	backtrack(nums, nil, &ans)

	return ans
}

func backtrack(nums []int, prev []int, ans *[][]int) {
	if len(nums) == 0 {
		*ans = append(*ans, append([]int{}, prev...))
		return
	}

	for i := 0; i < len(nums); i++ {
		backtrack(append(append([]int{}, nums[0:i]...), nums[i+1:]...),
			append(prev, nums[i]),
			ans)
	}
}