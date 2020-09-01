func containsPattern(arr []int, m int, k int) bool {
	count := 0
	for i := 0; i+m < len(arr); i++ {
		if arr[i] == arr[i+m] {
			count++
		} else {
			count = 0
		}
		if count == (k-1)*m {
			return true
		}
	}

	return false
}