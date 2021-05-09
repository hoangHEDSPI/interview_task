from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0
        currentAlt = 0
        for i in range(len(gain)):
            nextAlt = currentAlt + gain[i]
            currentAlt = nextAlt
            if nextAlt > maxAlt:
                maxAlt = nextAlt
        return maxAlt

if __name__ == '__main__':
    sol = Solution()
    gain = [-5,1,5,0,-7]
    assert sol.largestAltitude(gain) == 1
    gain = [-4,-3,-2,-1,4,3,2]
    assert sol.largestAltitude(gain) == 0
