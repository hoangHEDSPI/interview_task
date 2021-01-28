from typing import List

class Solution:
    # TLE
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sorted_pattern = sorted(p)
        ans = []
        len_p = len(p)
        for i in range(len(s)):
            if sorted(s[i:i+len_p]) == sorted_pattern:
                ans.append(i)
        return ans