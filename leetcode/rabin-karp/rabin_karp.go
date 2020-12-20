package rabin_karp

const base = 16777619

func hash(s string) uint32 {
	var h uint32
	for i := 0; i < len(s); i++ {
		h = (h*base + uint32(s[i]))
	}
	return h
}

func hashPatterns(patterns []string, l int) map[uint32][]int {
	m := make(map[uint32][]int)
	for i, t := range patterns {
		h := hash(t[:l])
		if _, ok := m[h]; ok {
			m[h] = append(m[h], i)
		} else {
			m[h] = []int{i}
		}
	}

	return m
}
