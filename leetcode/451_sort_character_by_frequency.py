from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        _sCounter = Counter(s)
        res = ''
        sortedCounter = {k: v for k, v in sorted(_sCounter.items(), key=lambda item: item[1], reverse=True)}
        for c in sortedCounter:
            for _ in range(sortedCounter[c]):
                res += c
        return res

if __name__ == '__main__':
    s = 'tree'
    sol = Solution()
    assert sol.frequencySort(s) == 'eert' or sol.frequencySort(s) == 'eetr'