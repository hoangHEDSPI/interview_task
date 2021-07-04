func max(a int, b int) int {
    if a >= b {
        return a
    }
    return b
}

func jump(nums []int) int {
    n := len(nums)
    start := 0
    end := 0
    step := 0
    for (end < n-1) {
        step += 1
        maxend := end + 1
        for i := start; i < end + 1; i++ {
            if i + nums[i] >= n-1 {
                return step
            }
            maxend = max(maxend, i + nums[i])
        }
        start = end + 1
        end = maxend
    }
    return step
}
