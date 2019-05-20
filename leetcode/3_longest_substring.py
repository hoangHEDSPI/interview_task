class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashset = set()
        ans = 0
        n = len(s)
        i = 0
        j = 0
        while i < n and j < n:
            if s[j] not in hashset:
                hashset.add(s[j])
                j += 1
                ans = max(ans, j-i)
            else:
                hashset.remove(s[i])
                i += 1
        return ans
