from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i-anchor+1)
                anchor = i+1
        return ans


if __name__ == "__main__":
    S = 'abccaddbeffe'
    sol = Solution()
    assert sol.partitionLabels(S)==[8, 4]