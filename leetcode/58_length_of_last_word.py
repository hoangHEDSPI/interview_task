class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        s = s.split(" ")
        return len(s[len(s)-1])
        