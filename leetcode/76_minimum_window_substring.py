from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        l, r = 0, 0
        # Dictionary which keeps a count of all the unique characters in t
        dict_t = Counter(t)
        required = len(dict_t)
        formed = 0
        window_counts = {}
        # Form ans as a tuple
        ans = float("inf"), None, None
        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            while l <= r and formed == required:
                character = s[l]
                if r-l+1 < ans[0]:
                    ans = (r-l+1, l, r)
                
if __name__ == "__main__":
    s = 'ADOBECODEBANC'
    t = 'ABC'
    sol = Solution()
    print(sol.minWindow(s, t))