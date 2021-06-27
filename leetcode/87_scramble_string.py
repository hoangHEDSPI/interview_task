class Solution:
    def __init__(self):
        self.memoization = {}
    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self.memoization:
            return self.memoization[(s1, s2)]
        
        if s1 == s2:
            self.memoization[(s1, s2)] = True
            return True
        
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        self.memoization[(s1, s2)] = False
        return False
        
