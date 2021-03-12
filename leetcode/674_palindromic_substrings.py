class Solution:
    def countSubstrings(self, s: str) -> int:
        len_s = len(s)
        ans = len_s
        states = [[False for _ in range(len_s)] for _ in range(len_s)]
        for i in range(len_s):
            states[i][i] = True
        for i in range(len_s-1):
            states[i][i+1] = (s[i] == s[i+1])
            ans += states[i][i+1]
        
        for k in range(3, len_s+1):
            for i in range(len_s-k+1):
                j = i+k-1
                states[i][j] = (states[i+1][j-1] and s[i] == s[j])
                ans += states[i][j]
        return ans 


if __name__ == '__main__':
    s = "aaaaa"
    sol = Solution()
    print(sol.countSubstrings(s))