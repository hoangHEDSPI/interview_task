// Go with O(n^2) first
func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}
func largestRectangleArea(heights []int) int {
	if len(heights) == 0 {
		return 0
	}
	if len(heights) == 1 {
		return heights[0]
	}
	lenHeights := len(heights)
	lessFromRight := make([]int, lenHeights)
	lessFromLeft := make([]int, lenHeights)
	lessFromRight[lenHeights-1] = lenHeights
	lessFromLeft[0] = -1

	for i := 1; i < lenHeights; i++ {
		p := i - 1
		for p >= 0 && heights[p] >= heights[i] {
			p = lessFromLeft[p]
		}
		lessFromLeft[i] = p
	}

	for i := lenHeights - 2; i >= 0; i-- {
		p := i + 1
		for p < lenHeights && heights[p] >= heights[i] {
			p = lessFromRight[p]
		}
		lessFromRight[i] = p
	}

	res := 0
	for i := 0; i < lenHeights; i++ {
		res = max(res, heights[i]*(lessFromRight[i]-lessFromLeft[i]-1))
	}
	return res

}